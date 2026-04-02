# docs
# https://docs.pytest.org/en/stable/getting-started.html

mkdir project_name
cd project_name

python3 -m venv .venv
source .venv/bin/activate

# optional
curl -L -O https://raw.githubusercontent.com/github/gitignore/refs/heads/main/Python.gitignore
mv Python.gitignore .gitignore

pip install -U pytest
pytest --version

mkdir tests
cd tests
touch test_sample.py

pytest
pytest -v  tests/test_sample.py
pytest tests/test_sample.py::test_case1
