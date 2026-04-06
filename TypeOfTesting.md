🏗️ 1. Folder Structure (Industry Standard)
```
project/
│
├── app/
│   ├── main.py
│   ├── services/
│   │     user_service.py
│   ├── api/
│   │     user_api.py
│   └── db/
│         models.py
│
├── tests/
│   ├── unit/
│   │     test_user_service.py
│   │
│   ├── integration/
│   │     test_user_api.py
│   │
│   ├── system/
│   │     test_system_flow.py
│   │
│   ├── e2e/
│   │     test_user_journey.py
│   │
│   ├── regression/
│   │     test_regression_suite.py
│   │
│   └── conftest.py

```


🧪 2. UNIT TEST (isolated logic)

👉 Test only function (no DB, no API)
```
# tests/unit/test_user_service.py

from app.services.user_service import get_full_name

def test_get_full_name():
    result = get_full_name("Gayathri", "A")
    assert result == "Gayathri A"
```
Example service:

# app/services/user_service.py
```
def get_full_name(first, last):
    return f"{first} {last}"
```
🔗 3. INTEGRATION TEST (API + DB)

👉 Tests interaction between components

# tests/integration/test_user_api.py
```
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_user():
    response = client.post("/users", json={
        "name": "Gayathri",
        "email": "Devi"
    })

    assert response.status_code == 200
    assert response.json()["name"] == "Gayathri"
```
🏢 4. SYSTEM TEST (full backend system)

👉 Runs full backend like real environment

# tests/system/test_system_flow.py
```
import requests

BASE_URL = "http://localhost:8000"

def test_full_backend_flow():
    # Create user
    res = requests.post(f"{BASE_URL}/users", json={
        "name": "System User",
        "email": "sys@test.com"
    })
    assert res.status_code == 200

    user_id = res.json()["id"]

    # Fetch user
    res2 = requests.get(f"{BASE_URL}/users/{user_id}")
    assert res2.status_code == 200
```
🌐 5. E2E TEST (frontend + backend)

👉 Real user journey (UI automation)

# tests/e2e/test_user_journey.py
```
from playwright.sync_api import Page, expect

def test_user_login_flow(page: Page):
    page.goto("https://example.com/login")

    page.fill("#username", "demo_user")
    page.fill("#password", "password123")
    page.click("button[type='submit']")

    expect(page).to_have_url("https://example.com/dashboard")
    expect(page.locator("h1")).to_have_text("Dashboard")
```
🔁 6. REGRESSION TEST (critical flows)

👉 Collection of important tests

# tests/regression/test_regression_suite.py
```
import pytest
from playwright.sync_api import Page, expect

@pytest.mark.regression
def test_login_regression(page: Page):
    page.goto("https://example.com/login")

    page.fill("#username", "demo_user")
    page.fill("#password", "password123")
    page.click("button[type='submit']")

    expect(page).to_have_url("https://example.com/dashboard")


@pytest.mark.regression
def test_dashboard_regression(page: Page):
    page.goto("https://example.com/dashboard")
    expect(page.locator("h1")).to_have_text("Dashboard")
```
Run only regression:
```
pytest -m regression
```
⚙️ 7. conftest.py (shared setup)
```
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        yield page
        browser.close()
```
🧠 Final Understanding (VERY IMPORTANT)

| Type        | Scope              | Speed   | Example           |
| ----------- | ------------------ | ------- | ----------------- |
| Unit        | Function           | ⚡ Fast  | get_full_name     |
| Integration | API + DB           | ⚡⚡      | create user       |
| System      | Full backend       | ⚡⚡⚡     | API flow          |
| E2E         | UI + Backend       | 🐢 Slow | login flow        |
| Regression  | Critical flows set | Mixed   | login + dashboard |

🔥 Real Industry Insight (for you)

👉 Best practice:
```
70% Unit tests
20% Integration
5% System
5% E2E
```
