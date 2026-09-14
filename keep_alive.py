from playwright.sync_api import sync_playwright

APPS = [
    "https://bambas.streamlit.app/",
    "https://calculadorabambas.streamlit.app/",
    "https://pdetalles.streamlit.app/",
]

def visit(url):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url, timeout=60000)
        page.wait_for_timeout(5000)

        try:
            wake_button = page.get_by_text("get this app back up", exact=False)
            if wake_button.is_visible(timeout=3000):
                wake_button.click()
                print(f"Encontrada dormida, despertando: {url}")
                page.wait_for_timeout(15000)
        except Exception:
            pass

        print(f"Visitada correctamente: {url}")
        browser.close()

for app in APPS:
    try:
        visit(app)
    except Exception as e:
        print(f"Error visitando {app}: {e}")
