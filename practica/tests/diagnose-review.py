"""Diagnóstico temporal de la revisión tras completar MAP-DEMO-005."""
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 320, "height": 850})
    page_errors = []
    page.on("pageerror", lambda error: page_errors.append(str(error)))
    page.goto("http://127.0.0.1:8765/practica/index.html", wait_until="load")
    page.locator("#settings-panel > summary").click()
    page.locator("#area").select_option("algebra")
    page.locator("#apply-settings").click()
    page.locator("#settings-panel > summary").click()
    page.locator("#new").click()
    for key in [0, 1, 2, 1]:
        page.locator("#question input[name='answer']").nth(key).check()
        page.locator("#submit").click()
    page.evaluate("""() => {
      window.__reviewLog = [];
      const button = document.querySelector('#trace button[data-step]');
      button.addEventListener('click', () => __reviewLog.push('button listener (test)'));
      document.querySelector('#trace').addEventListener('click', e => __reviewLog.push('trace delegated '+e.target.tagName));
      document.addEventListener('click', e => __reviewLog.push('document '+e.target.tagName));
      new MutationObserver(mutations => {
        for (const m of mutations) __reviewLog.push('mutation '+m.target.id+' '+m.attributeName+' '+m.target.getAttribute(m.attributeName));
      }).observe(document.querySelector('#review'), {attributes: true, attributeFilter:['hidden']});
    }""")
    def inspect(label):
        print(label, page.evaluate("""() => {
          const review = document.querySelector('#review');
          const trace = document.querySelector('#trace');
          return {reviewHidden:review.hidden,display:getComputedStyle(review).display,
           detailsOpen:document.querySelector('#trace-disclosure').open,
           traceChildren:trace.children.length,
           buttonConnected:trace.querySelector('button').isConnected,
           button:trace.querySelector('button').outerHTML.slice(0,450),
           selected:trace.querySelector('[aria-current]')?.outerHTML.slice(0,80),
           log:window.__reviewLog};
        }"""))
        print('JS_ERRORS', page_errors)
    inspect('BEFORE')
    page.locator("#trace button[data-step]").first.click()
    page.wait_for_timeout(100)
    inspect('AFTER PLAYWRIGHT CLICK')
    page.evaluate("document.querySelector('#trace button[data-step]').click()")
    page.wait_for_timeout(100)
    inspect('AFTER JS CLICK')
    browser.close()
