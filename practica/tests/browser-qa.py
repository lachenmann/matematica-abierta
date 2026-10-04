"""Prueba reproducible en Chromium: diez problemas por ancho, MathJax y Elo.
Ejecutar desde la raíz con servidor HTTP en 127.0.0.1:8765.
"""
from pathlib import Path
from playwright.sync_api import sync_playwright

BASE = "http://127.0.0.1:8765/practica/index.html"
OUT = Path("practica/browser-qa-artifacts")
OUT.mkdir(parents=True, exist_ok=True)
KEYS = {
    "MAP-DEMO-005": [0, 1, 2, 1], "MAP-DEMO-006": [1, 0, 2],
    "MAP-DEMO-007": [2, 0, 1], "MAP-DEMO-008": [1, 2, 0],
    "MAP-DEMO-009": [0, 1, 2], "MAP-DEMO-010": [1, 2, 0],
    "MAP-DEMO-011": [2, 0, 1], "MAP-DEMO-012": [1, 0, 2, 1],
    "MAP-DEMO-013": [1, 0, 2], "MAP-DEMO-014": [2, 0, 1],
}
TITLES = (
    "Ecuación con fracciones", "Una identidad", "Ecuación incompatible",
    "Extraer factor común", "Diferencia de cuadrados", "Producto igual a cero",
    "Inecuación y signo", "Ecuación racional", "Sistema por eliminación",
    "Las dos raíces",
)


def contrast_ratio(page, foreground, background):
    return page.evaluate("""([foreground, background]) => {
      const channels = color => {
        const hex = color.trim().match(/^#([0-9a-f]{3}|[0-9a-f]{6})$/i);
        const values = hex
          ? (hex[1].length === 3 ? [...hex[1]].map(value => value + value) : hex[1].match(/../g))
              .map(value => parseInt(value, 16))
          : color.match(/[\\d.]+/g).slice(0, 3).map(Number);
        return values
        .map(value => value / 255)
        .map(value => value <= .04045 ? value / 12.92 : ((value + .055) / 1.055) ** 2.4);
      };
      const luminance = color => {
        const [r, g, b] = channels(color);
        return .2126 * r + .7152 * g + .0722 * b;
      };
      const a = luminance(foreground), b = luminance(background);
      return (Math.max(a, b) + .05) / (Math.min(a, b) + .05);
    }""", [foreground, background])


def is_focused(locator):
    return locator.evaluate("element => element === document.activeElement")


def audit_contrast(page, scheme):
    page.emulate_media(color_scheme=scheme)
    colors = page.evaluate("""() => {
      const style = getComputedStyle(document.documentElement);
      return Object.fromEntries(['--paper', '--ink', '--muted', '--brand', '--brand-ink',
        '--good', '--bad', '--control-border', '--focus'].map(name => [name, style.getPropertyValue(name).trim()]));
    }""")
    for token in ('--ink', '--muted', '--brand', '--good', '--bad'):
        ratio = contrast_ratio(page, colors[token], colors['--paper'])
        assert ratio >= 4.5, f"{scheme} {token}: contraste de texto {ratio:.2f}:1"
    primary = page.locator("#submit").evaluate("""element => {
      const style = getComputedStyle(element);
      return [style.color, style.backgroundColor];
    }""")
    assert contrast_ratio(page, primary[0], primary[1]) >= 4.5
    assert contrast_ratio(page, colors['--control-border'], colors['--paper']) >= 3
    assert contrast_ratio(page, colors['--focus'], colors['--paper']) >= 3


def no_overflow(page, label):
    sizes = page.evaluate("""() => [innerWidth,
       document.documentElement.scrollWidth, document.body.scrollWidth]""")
    assert max(sizes[1:]) <= sizes[0] + 1, f"{label}: overflow horizontal {sizes}"


def math_ready(page, label):
    page.wait_for_function("""() => window.MathJax &&
      typeof MathJax.typesetPromise === 'function' &&
      !document.querySelector('#workspace [data-math-pending="true"]')""", timeout=45000)
    # Un enunciado puede contener varias ecuaciones (p. ej. un sistema 2x2).
    page.locator("#prompt mjx-container").first.wait_for(timeout=25000)
    assert page.locator("#prompt mjx-math").count() >= 1, f"{label}: MathJax no compuso el enunciado"


def select_algebra(page, challenge=False):
    page.locator("#title").wait_for()
    page.locator("#settings-panel > summary").click()
    page.locator("#area").select_option("algebra")
    if challenge:
        page.locator("#mode").select_option("challenge")
    else:
        page.locator("#apply-settings").click()
    assert page.locator("#title").inner_text() == "Resolver una ecuación"
    page.locator("#settings-panel > summary").click()
    page.locator("#new").click()
    assert page.locator("#title").inner_text() == TITLES[0]


def solve(page, exercise_id, keys, width):
    assert page.locator("#title").inner_text() == TITLES[int(exercise_id[-3:]) - 5]
    math_ready(page, f"{width} {exercise_id} inicio")
    for i, key in enumerate(keys):
        page.locator("#question input[name='answer']").nth(key).check()
        page.locator("#submit").click()
        page.wait_for_function("""n => Number(document.querySelector('#stepsbar')
           .getAttribute('aria-valuenow')) === n""", arg=i + 1)
        assert page.locator("#trace button[data-step]").count() == i + 1
        math_ready(page, f"{width} {exercise_id} paso {i+1}")
        no_overflow(page, f"{width} {exercise_id} paso {i+1}")
    assert page.locator("#another").is_visible()
    assert "aciertos al primer intento" in page.locator("#question").inner_text()
    # Clic físico en el centro de la fila, frecuentemente ocupado por una fórmula MathJax.
    page.locator("#trace button[data-step]").first.click()
    assert page.locator("#review").is_visible()
    assert "Primera elección" in page.locator("#review-choice").inner_text()
    page.locator("#review-return").click()
    assert page.locator("#review").is_hidden()
    no_overflow(page, f"{width} {exercise_id} revisión")


def viewport(browser, width):
    ctx = browser.new_context(viewport={"width": width, "height": 850}, reduced_motion="reduce", locale="es-CL")
    page = ctx.new_page()
    errors = []
    page.on("pageerror", lambda error: errors.append(str(error)))
    try:
        page.goto(BASE, wait_until="load", timeout=60000)
        select_algebra(page)
        for exercise_id, keys in KEYS.items():
            solve(page, exercise_id, keys, width)
            if exercise_id in {"MAP-DEMO-005", "MAP-DEMO-012", "MAP-DEMO-014"}:
                page.screenshot(path=str(OUT / f"algebra-{width}-{exercise_id}.png"), full_page=True)
            if exercise_id != "MAP-DEMO-014":
                page.locator("#another").click()
        page.locator("#history-toggle").click()
        assert page.locator("#history-panel").is_visible()
        assert page.locator("#past > li").count() >= 10
        page.locator("#history-toggle").click()
        assert page.locator("#title").inner_text() == TITLES[-1]
        no_overflow(page, f"{width} historial")
        assert not errors, f"{width} errores JavaScript: {errors}"
        print(f"PASS {width}px: 10 problemas, 32 decisiones, MathJax, planilla, historial")
    finally:
        ctx.close()


def wrong_attempt(browser):
    ctx = browser.new_context(viewport={"width": 375, "height": 850}, locale="es-CL")
    page = ctx.new_page()
    try:
        page.goto(BASE, wait_until="load", timeout=60000)
        select_algebra(page, challenge=True)
        original = page.locator("#rating-current").inner_text()
        page.locator("#question input[name='answer']").nth(1).check()
        page.locator("#submit").click()
        assert page.locator("#retry").is_visible()
        assert page.locator("#give-up").is_visible()
        page.locator("#retry").click()
        for i, key in enumerate(KEYS["MAP-DEMO-005"]):
            page.locator("#question input[name='answer']").nth(key).check()
            page.locator("#submit").click()
            if i == 0:
                page.locator("#trace button[data-step]").first.click()
                assert "primer intento fallido" in page.locator("#review-title").inner_text().lower()
                page.locator("#review-return").click()
        summary = page.locator("#question").inner_text()
        assert "3/4 aciertos al primer intento" in summary, summary
        assert "Desafío con al menos un error inicial" in summary, summary
        assert page.locator("#rating-current").inner_text() != original
        page.locator("#history-toggle").click()
        page.locator("#past > li").first.locator("summary").click()
        assert "Errores registrados en los pasos: 1" in page.locator("#past").inner_text()
        print("PASS desafío: fallo inicial, reintento, corrección, Elo e historial")
    finally:
        ctx.close()


def keyboard_and_semantics(browser):
    ctx = browser.new_context(viewport={"width": 375, "height": 850}, locale="es-CL")
    page = ctx.new_page()
    try:
        page.goto(BASE, wait_until="load", timeout=60000)
        assert page.evaluate("document.activeElement.id") == "title"
        page.keyboard.press("Shift+Tab")
        assert is_focused(page.locator("#settings-panel > summary"))
        page.keyboard.press("Enter")
        page.keyboard.press("Tab")
        assert page.evaluate("document.activeElement.id") == "area"
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("Tab")
        assert page.evaluate("document.activeElement.id") == "mode"
        page.keyboard.press("ArrowDown")
        assert page.locator("#title").inner_text() == "Resolver una ecuación"
        assert page.evaluate("document.activeElement.id") == "title"
        assert page.locator("#stepsbar").get_attribute("aria-valuetext") == "0 de 3 pasos completados"
        assert page.locator("#question [role=radiogroup]").get_attribute("aria-labelledby") == "question-title"

        page.keyboard.press("Tab")
        assert is_focused(page.locator("#question input[name=answer]").first)
        page.keyboard.press("Space")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowUp")
        page.keyboard.press("Tab")
        assert is_focused(page.locator("#submit"))
        page.keyboard.press("Enter")
        assert page.evaluate("document.activeElement.id") == "question-title"
        assert page.locator("#stepsbar").get_attribute("aria-valuetext") == "1 de 3 pasos completados"

        page.locator("#trace button[data-step]").first.focus()
        page.keyboard.press("Enter")
        assert page.evaluate("document.activeElement.id") == "review-title"
        page.locator("#review-return").focus()
        page.keyboard.press("Space")
        assert is_focused(page.locator("#trace button[data-step]").first)

        # Error, reintento y corrección del segundo paso, solo con teclado.
        page.locator("#question input[name=answer]").first.focus()
        page.keyboard.press("ArrowDown")
        page.keyboard.press("Tab")
        page.keyboard.press("Enter")
        assert page.locator("#retry").is_visible()
        active_id = page.evaluate("document.activeElement.id")
        assert active_id == "retry", f"foco tras error: {active_id}"
        page.keyboard.press("Space")
        assert is_focused(page.locator("#question input[name=answer]").first)
        page.keyboard.press("Space")
        page.keyboard.press("Tab")
        page.keyboard.press("Enter")
        assert page.evaluate("document.activeElement.id") == "question-title"

        # Rendición del tercer paso y continuación desde el mensaje anunciado.
        page.keyboard.press("Tab")
        page.keyboard.press("Space")
        page.keyboard.press("Tab")
        page.keyboard.press("Enter")
        active_id = page.evaluate("document.activeElement.id")
        assert active_id == "retry", f"foco antes de rendirse: {active_id}"
        page.keyboard.press("Tab")
        assert page.evaluate("document.activeElement.id") == "give-up"
        page.keyboard.press("Enter")
        assert page.evaluate("document.activeElement.id") == "feedback"
        assert page.locator("#feedback").get_attribute("role") == "status"
        page.keyboard.press("Shift+Tab")
        assert page.evaluate("document.activeElement.id") == "next"
        page.keyboard.press("Enter")
        assert page.locator("#another").is_visible()
        assert page.evaluate("document.activeElement.id") == "question-title"

        page.locator("#history-toggle").focus()
        page.keyboard.press("Enter")
        assert page.evaluate("document.activeElement.id") == "history-title"
        page.locator("#history-toggle").focus()
        page.keyboard.press("Space")
        assert page.evaluate("document.activeElement.id") == "title"
        audit_contrast(page, "light")
        audit_contrast(page, "dark")
        print("PASS teclado y semántica: Tab, Shift+Tab, Enter, espacio, flechas, foco y contraste")
    finally:
        ctx.close()


def mathjax_failure_modes(browser):
    # MathJax local bloqueado: la carga termina y el flujo esencial sigue operativo con texto de reserva.
    blocked = browser.new_context(viewport={"width": 375, "height": 850}, locale="es-CL")
    page = blocked.new_page()
    page.route("**/vendor/mathjax/**", lambda route: route.abort())
    try:
        page.goto(BASE, wait_until="load", timeout=10000)
        select_algebra(page)
        assert page.locator("#prompt mjx-container").count() == 0
        assert page.locator("#prompt").inner_text() == "Resuelve (x-1)/3+(x+2)/2=4."
        page.locator("#question input[name=answer]").first.check()
        page.locator("#submit").click()
        assert page.locator("#trace button[data-step]").count() == 1
        page.locator("#history-toggle").click()
        assert page.locator("#history-panel").is_visible()
    finally:
        blocked.close()

    # La biblioteca llega a iniciar, pero su composición rechaza la promesa.
    failed = browser.new_context(viewport={"width": 375, "height": 850}, locale="es-CL")
    page = failed.new_page()
    stub = """Object.assign(window.MathJax, {
      startup: { promise: Promise.resolve() }, typesetClear() {},
      typesetPromise() { return Promise.reject(new Error('fallo simulado de MathJax')); }
    });"""
    page.route("**/vendor/mathjax/**", lambda route: route.fulfill(status=200,
        content_type="application/javascript", body=stub))
    try:
        page.goto(BASE, wait_until="load", timeout=10000)
        select_algebra(page)
        page.wait_for_timeout(100)
        assert page.locator("#prompt").inner_text() == "Resuelve (x-1)/3+(x+2)/2=4."
        assert page.locator("#prompt").get_attribute("data-math-pending") == "true"
        page.locator("#question input[name=answer]").first.check()
        page.locator("#submit").click()
        assert page.locator("#trace button[data-step]").count() == 1
    finally:
        failed.close()
    print("PASS MathJax local: recurso bloqueado y fallo posterior conservan texto y flujo esencial")


if __name__ == "__main__":
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        try:
            for width in (320, 375, 430, 1280):
                viewport(browser, width)
            wrong_attempt(browser)
            keyboard_and_semantics(browser)
            mathjax_failure_modes(browser)
        finally:
            browser.close()
    print("PASS: 40 recorridos y 128 decisiones; teclado completo; MathJax local normal, bloqueado y fallido")
