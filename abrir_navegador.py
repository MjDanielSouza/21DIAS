"""
Script para abrir o Chrome já autenticado no Clube do Segredo.
Execute com: python abrir_navegador.py
"""

from playwright.sync_api import sync_playwright

PROFILE_DIR = r"d:\ANDREIA\chrome_profile"
TARGET_URL = "https://clubedosegredo.vercel.app/jornada"

def main():
    print("Iniciando navegador autenticado...")
    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir=PROFILE_DIR,
            channel="chrome",
            headless=False,
            args=["--start-maximized"]
        )
        page = context.pages[0] if context.pages else context.new_page()
        page.goto(TARGET_URL)
        print("Página aberta! Pressione Ctrl+C no terminal quando terminar para fechar.")
        page.wait_for_timeout(3600000) # mantem aberto

if __name__ == "__main__":
    main()
