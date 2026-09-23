"""QA de MA-Práctica en Chromium real. Ejecutar desde la raíz del repositorio.

Requiere un servidor HTTP local en 127.0.0.1:8765 y playwright+Chromium.
No modifica el progreso ni el banco de ejercicios en el repositorio.
"""
from pathlib import Path
from playwright.sync_api import sync_playwright

BASE = "http://127.0.0.1:8765/practica/index.html"
OUT = Path("practica/browser-qa-artifacts")
OUT.mkdir(parents=True, exist_ok=True)
KEYS = {
    "MAP-DEMO-005": [0, 1, 2, 1],
    "MAP-DEMO-006": [1, 0, 2],
    "MAP-DEMO-007": [2, 0, 1],
    "MAP-DEMO-008": [1, 2, 0],
    "MAP-DEMO-009": [0, 1, 2],
    "MAP-DEMO-010": [1, 2, 0],
    "MAP-DEMO-011": [2, 0, 1],
    "MAP-DEMO-012": [1, 0, 2, 1],
    "MAP-DEMO-013": [1, 0, 2],
    "MAP-DEMO-014": [2, 0, 1],
}
TITLES = [
    "Ecuación con fracciones", "Una identidad", "Ecuación incompatible",
    "Extraer factor común", "Diferencia de cuadrados", "Producto igual a cero",
    "Inecuación y signo", "Ecuación racional", "Sistema por eliminación",
    "Las dos raíces",
]


def no_page_overflow(page, context):
    dims = page.evaluate("""() => ({width: innerWidth,
      document: document.documentElement.scrollWidth,
      body: document.body.scrollWidth})""")
    assert dims["document"] <= dims["width"] + 1, f"{context}: horizontal overflow {dims}"
    assert dims["body"] <= dims["width"] + 1, f"{context}: body overflow {dims}"


def typeset_ready(page, context):
    page.wait_for_function("""() => window.MathJax &&
       typeof MathJax.typesetPromise === 'function' &&
       !document.querySelector('#workspace [data-math-pending="true"]')""", timeout=45000)
    # No basta con que el CDN responda: debe haberse compuesto la expresión del problema.
    page.locator("#prompt mjx-container").wait_for(timeout=20000)
    assert page.locator("#prompt mjx-math").count() >= 1, f"{context}: TeX no compuesto"


def navigate_to_algebra(page, mode="training"):
    page.locator("#title").wait_for()
    page.locator("#settings-panel > summary").click()
    page.locator("#area").select_option("algebra")
    if mode != "training":
        page.locator("#mode").select_option(mode)
    else:
        page.locator("#apply-settings").click()
    assert page.locator("#title").inner_text() == "Resolver una ecuación"
    # El primer ejercicio original de Álgebra sigue existiendo y precede al lote.
    page.locator("#settings-panel > summary").click()
    page.locator("#new").click()
    assert page.locator("#title").inner_text() == TITLES[0]


def finish_problem(page, exercise_id, keys, width):
    title = TITLES[int(exercise_id[-3:]) - 5]
    assert page.locator("#title").inner_text() == title, exercise_id
    typeset_ready(page, f"{width}px {exercise_id} inicio")
    for index, key in enumerate(keys):
        page.locator("#question input[name='answer']").nth(key).check()
        assert page.locator("#submit").is_enabled()
        page.locator("#submit").click()
        expected = index + 1
        page.wait_for_function("""expected => Number(document.querySelector('#stepsbar').getAttribute('aria-valuenow')) === expected""", expected)
        assert page.locator("#trace button[data-step]").count() == expected
        if index + 1 < len(keys):
            assert f"Paso {index+2} de {len(keys)}" in page.locator("#progress").inner_text()
        typeset_ready(page, f"{width}px {exercise_id} paso {expected}")
        no_page_overflow(page, f"{width}px {exercise_id} paso {expected}")
    assert page.locator("#another").is_visible()
    assert "aciertos al primer intento" in page.locator("#question").inner_text()
    assert page.locator("#trace button[data-step]").count() == len(keys)
    # Revisar una jugada es de solo lectura; el regreso mantiene la sesión completada.
    page.locator("#trace button[data-step]").first.click()
    assert page.locator("#review").is_visible()
    assert "Primera elección" in page.locator("#review-choice").inner_text()
    page.locator("#review-return").click()
    assert page.locator("#review").is_hidden()
    no_page_overflow(page, f"{width}px {exercise_id} revisión")


def run_viewport(browser, width):
    context = browser.new_context(viewport={"width": width, "height": 850}, reduced_motion="reduce", locale="es-CL")
    page = context.new_page()
    errors = []
    page.on("pageerror", lambda err: errors.append(str(err)))
    try:
        page.goto(BASE, wait_until="load", timeout=60000)
        navigate_to_algebra(page)
        for exercise_id, keys in KEYS.items():
            finish_problem(page, exercise_id, keys, width)
            if exercise_id in {"MAP-DEMO-005", "MAP-DEMO-012", "MAP-DEMO-014"}:
                page.screenshot(path=str(OUT / f"algebra-{width}-{exercise_id}.png"), full_page=True)
            if exercise_id != "MAP-DEMO-014":
                page.locator("#another").click()
        # El historial es local y permite recuperar el último ejercicio.
        page.locator("#history-toggle").click()
        assert page.locator("#history-panel").is_visible()
        assert page.locator("#past > li").count() >= 10
        page.locator("#history-toggle").click()
        assert page.locator("#title").inner_text() == TITLES[-1]
        no_page_overflow(page, f"{width}px historial y vuelta")
        assert not errors, f"{width}px errores JavaScript: {errors}"
        print(f"PASS viewport={width}: 10 ejercicios, 32 pasos, MathJax real, planilla e historial")
    finally:
        context.close()


def run_wrong_attempt(browser):
    context = browser.new_context(viewport={"width": 375, "height": 850}, reduced_motion="reduce", locale="es-CL")
    page = context.new_page()
    try:
        page.goto(BASE, wait_until="load", timeout=60000)
        navigate_to_algebra(page, mode="challenge")
        before = page.locator("#rating-current").inner_text()
        # Primer error intencional: la corrección no puede convertirlo en acierto inicial.
        page.locator("#question input[name='answer']").nth(1).check()
        page.locator("#submit").click()
        assert page.locator("#retry").is_visible()
        assert page.locator("#give-up").is_visible()
        page.locator("#retry").click()
        for index, key in enumerate(KEYS["MAP-DEMO-005"]):
            page.locator("#question input[name='answer']").nth(key).check()
            page.locator("#submit").click()
            if index == 0:
                page.locator("#trace button[data-step]").first.click()
                assert "primer intento fallido" in page.locator("#review-title").inner_text().lower()
                page.locator("#review-return").click()
        summary = page.locator("#question").inner_text()
        assert "3/4 aciertos al primer intento" in summary, summary
        assert "Desafío con al menos un error inicial" in summary, summary
        assert page.locator("#rating-current").inner_text() != before
        page.locator("#history-toggle").click()
        assert "Errores registrados en los pasos: 1" in page.locator("#past").inner_text()
        print("PASS: error inicial, reintento, trazabilidad, Elo experimental e historial")
    finally:
        context.close()


if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        try:
            for width in (320, 375, 430, 1280):
                run_viewport(browser, width)
            run_wrong_attempt(browser)
        finally:
            browser.close()
    print("PASS browser-qa: 40 recorridos completos; 128 decisiones, flujos y screenshots")
