from playwright.sync_api import sync_playwright

APPS = [
    "https://pdetalles.streamlit.app/",
    "https://bambas.streamlit.app/",
    "https://calculadorabambas.streamlit.app/",
]

def visit(url):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url, timeout=60000)
        page.wait_for_timeout(8000)
        print(f"Visitada correctamente: {url}")
        browser.close()

for app in APPS:
    try:
        visit(app)
    except Exception as e:
        print(f"Error visitando {app}: {e}")
