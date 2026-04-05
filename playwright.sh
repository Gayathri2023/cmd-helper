#!/bin/bash

#docs
#https://playwright.dev/python/docs/intro

mkdir playwright_full
cd playwright_full

# Virtual env
python3 -m venv .venv
source .venv/bin/activate

# Install
pip install --upgrade pip
pip install playwright pytest
playwright install

# Create folders
mkdir tests

# -----------------------------
# FULL EXAMPLE FILE
# -----------------------------
cat <<EOL > tests/test_all.py
from playwright.sync_api import sync_playwright

URL = "https://example.com"   # change this

def test_all_selectors():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        page.goto(URL)

        # -----------------------------
        # BASIC SELECTORS
        # -----------------------------
        print("=== BASIC SELECTORS ===")
        page.locator("button")  # tag
        page.locator("#id")     # id
        page.locator(".class")  # class

        # -----------------------------
        # TEXT SELECTORS
        # -----------------------------
        print("=== TEXT SELECTORS ===")
        page.get_by_text("Login")
        page.locator('text=Login')
        page.locator('button:has-text("Login")')

        # -----------------------------
        # ATTRIBUTE SELECTORS
        # -----------------------------
        print("=== ATTRIBUTE SELECTORS ===")
        page.locator('[type="submit"]')
        page.locator('[aria-label="Login"]')

        # -----------------------------
        # ROLE BASED (BEST)
        # -----------------------------
        print("=== ROLE SELECTORS ===")
        page.get_by_role("button", name="Login")

        # -----------------------------
        # FORM SELECTORS
        # -----------------------------
        print("=== FORM ===")
        page.locator("form button")

        # -----------------------------
        # FULL CSS (NOT RECOMMENDED)
        # -----------------------------
        print("=== FULL CSS ===")
        page.locator('#app > div > div > form > button')

        # -----------------------------
        # XPATH
        # -----------------------------
        print("=== XPATH ===")
        page.locator('//button[text()="Login"]')

        # -----------------------------
        # COUNT ELEMENTS
        # -----------------------------
        print("=== COUNT ===")
        print(page.locator("button").count())

        # -----------------------------
        # WAITING (JS LOAD)
        # -----------------------------
        print("=== WAIT ===")
        page.wait_for_selector("button", state="visible")

        # -----------------------------
        # CLICK (SAFE)
        # -----------------------------
        print("=== CLICK ===")
        if page.locator("button").count() > 0:
            page.locator("button").first.click()

        # -----------------------------
        # FORCE CLICK
        # -----------------------------
        print("=== FORCE CLICK ===")
        page.locator("button").first.click(force=True)

        # -----------------------------
        # INPUT HANDLING
        # -----------------------------
        print("=== INPUT ===")
        # page.fill('input[name="username"]', "user")

        # -----------------------------
        # IFRAME HANDLING
        # -----------------------------
        print("=== IFRAME ===")
        # frame = page.frame_locator("iframe")
        # frame.get_by_role("button").click()

        # -----------------------------
        # DEBUG MODE
        # -----------------------------
        print("=== DEBUG ===")
        page.pause()

        browser.close()
EOL

# -----------------------------
# RUN COMMAND
# -----------------------------
echo ""
echo "Run tests:"
echo "pytest -v"

echo ""
echo "Run debug mode:"
echo "PWDEBUG=1 pytest -s"

echo ""
echo "Open codegen:"
echo "playwright codegen https://example.com"
