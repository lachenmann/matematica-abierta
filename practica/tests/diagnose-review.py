"""Diagnóstico temporal: por qué no se abre la revisión tras finalizar MAP-DEMO-005."""
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width":320,"height":850})
    page_errors = []
    page.on("pageerror", lambda error: page_errors.append(str(error)))
    page.goto("http://127.0.0.1:8765/practica/index.html", wait_until="load")
    page.locator("#settings-panel > summary").click()
    page.locator("#area").select_option("algebra")
    page.locator("#apply-settings").click()
    page.locator("#settings-panel > summary").click()
    page.locator("#new").click()
    for key in [0,1,2,1]:
        page.locator("#question input[name='answer']").nth(key).check()
        page.locator("#submit").click()
    def inspect(label):
        print(label, page.evaluate("""() => {
         const review = document.querySelector('#review');
         const details = document.querySelector('#trace-disclosure');
         const trace = document.querySelector('#trace');
         return {completed:document.querySelector('#question').innerText,
          reviewHidden:review.hidden,reviewDisplay:getComputedStyle(review).display,
          reviewRect:review.getBoundingClientRect().toJSON(),detailsOpen:details.open,
          detailsDisplay:getComputedStyle(details).display,
          traceChildren:trace.children.length,firstClass:trace.children[0].className,
          workspaceHidden:document.querySelector('#workspace').hidden,
          focused:document.activeElement.id,selected:trace.querySelector('[aria-current]')?.getAttribute('aria-current')};
        }"""))
        print('JS_ERRORS', page_errors)
    inspect('BEFORE')
    page.locator("#trace button[data-step]").first.click()
    inspect('AFTER')
    browser.close()
