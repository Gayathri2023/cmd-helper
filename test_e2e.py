from playwright.sync_api import sync_playwright


def test_e2e_frontend_backend():
    with sync_playwright() as p:
        request = p.request.new_context()
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        base_url = "http://127.0.0.1:8000"

        # CREATE USER (Backend API)
        res = request.post(f"{base_url}/users", json={"name": "Gayathri", "job": "QA"})
        assert res.status == 200
        user_id = res.json()["id"]
        print("User Created:", user_id)

        # OPEN FRONTEND UI
        page.goto("file:///Users/yourname/Desktop/index.html")

        # CREATE USER FROM UI
        page.fill("#name", "Gayathri UI")
        page.fill("#job", "Tester")
        page.click("text=Create")
        page.wait_for_selector("#result")
        print("UI Result:", page.inner_text("#result"))

        # READ USER (Backend API)
        res = request.get(f"{base_url}/users/{user_id}")
        assert res.status == 200
        print("User Read:", res.json())

        # UPDATE USER (Backend API)
        res = request.put(f"{base_url}/users/{user_id}", json={"name": "Gayathri", "job": "Senior QA"})
        assert res.status == 200
        print("User Updated")

        # DELETE USER (Backend API)
        res = request.delete(f"{base_url}/users/{user_id}")
        assert res.status == 200
        print("User Deleted")

        browser.close()
