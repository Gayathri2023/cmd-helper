# docs
# https://fastapi.tiangolo.com/

mkdir project_name
cd project_name

python3 -m venv .venv
source .venv/bin/activate

# optional
curl -L -O https://raw.githubusercontent.com/github/gitignore/refs/heads/main/Python.gitignore
mv Python.gitignore .gitignore

pip install "fastapi[standard]"

touch main.py
uvicorn main:app --host 127.0.0.1 --port 1234
