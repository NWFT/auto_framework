import pytest


if __name__ == '__main__':
    pytest.main(["-s", "test_cases/example", "--alluredir=./reports/allure-report/"])

# > python -m pytest
