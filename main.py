import pytest

import settings

if __name__ == '__main__':
    pytest.main(["-s", "-v",
                 "--alluredir=./reports/allure-report/",
                 settings.TEST_CASES_DIR
                 ])


# > python -m pytest
