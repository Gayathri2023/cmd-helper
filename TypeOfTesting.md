🏗️ 1. Folder Structure (Industry Standard)

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
