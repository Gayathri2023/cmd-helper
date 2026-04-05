from playwright.sync_api import sync_playwright

def test_ui_crud():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Open demo CRUD website
        page.goto("https://example-crud-app.com")

        # ---------------- CREATE ----------------
        page.click("text=Add User")
        page.fill("#name", "Gayathri")
        page.fill("#email", "gayathri@test.com")
        page.click("text=Save")

        # Verify user created
        page.wait_for_selector("text=Gayathri")
        print("User Created")

        # ---------------- READ ----------------
        page.fill("#search", "Gayathri")
        page.click("text=Search")
        page.wait_for_selector("text=gayathri@test.com")
        print("User Read")

        # ---------------- UPDATE ----------------
        page.click("text=Edit")
        page.fill("#name", "Gayathri QA")
        page.click("text=Update")
        page.wait_for_selector("text=Gayathri QA")
        print("User Updated")

        # ---------------- DELETE ----------------
        page.click("text=Delete")
        page.click("text=Confirm")

        print("User Deleted")

        browser.close()
