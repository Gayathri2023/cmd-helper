import pytest
import sys

# -----------------------------
# 1. Basic Function & Test
# -----------------------------
def add(x, y):
    return x + y

def test_add():
    assert add(2, 3) == 5


# -----------------------------
# 2. Parameterization
# -----------------------------
@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (2, 3, 5),
    (5, 5, 10),
])
def test_add_param(a, b, expected):
    assert add(a, b) == expected


# -----------------------------
# 3. Fixture Example
# -----------------------------
@pytest.fixture
def sample_data():
    return {"name": "Gayathri", "age": 25}

def test_fixture(sample_data):
    assert sample_data["name"] == "Gayathri"


# -----------------------------
# 4. Fixture with Setup & Teardown
# -----------------------------
@pytest.fixture
def setup_teardown():
    print("\nSetup")
    yield "resource"
    print("\nTeardown")

def test_setup_teardown(setup_teardown):
    assert setup_teardown == "resource"


# -----------------------------
# 5. Skipping Tests
# -----------------------------
@pytest.mark.skip(reason="Skipping this test for demo")
def test_skip():
    assert False


# -----------------------------
# 6. Skip Based on Condition
# -----------------------------

@pytest.mark.skipif(sys.version_info < (3, 8), reason="Requires Python 3.8+")
def test_skip_condition():
    assert True


# -----------------------------
# 7. Expected Failure
# -----------------------------
@pytest.mark.xfail(reason="Known bug")
def test_expected_fail():
    assert add(2, 2) == 5


# -----------------------------
# 8. Exception Testing
# -----------------------------
def divide(a, b):
    return a / b

def test_exception():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)


# -----------------------------
# 9. Grouping Tests in Class
# -----------------------------
class TestMath:

    def test_add(self):
        assert add(1, 1) == 2

    def test_divide(self):
        assert divide(10, 2) == 5


# -----------------------------
# 10. Markers (Custom Tagging)
# -----------------------------
@pytest.mark.slow
def test_slow():
    assert add(100, 200) == 300


# -----------------------------
# 11. Using tmp_path (Built-in Fixture)
# -----------------------------
def test_tmp_file(tmp_path):
    file = tmp_path / "test.txt"
    file.write_text("hello")
    assert file.read_text() == "hello"


# -----------------------------
# 12. Multiple Assertions (Pytest Style)
# -----------------------------
def test_multiple():
    assert add(1, 2) == 3
    assert add(2, 2) == 4
    assert add(0, 0) == 0
