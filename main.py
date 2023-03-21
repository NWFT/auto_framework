import pytest

import settings

if __name__ == '__main__':
    pytest.main(["-s", "-v",
                 "--clean-alluredir",
                 "--alluredir=./reports/allure-report/",
                 "--reruns=0",
                 "-m smoke or regressions",
                 settings.TEST_CASES_DIR
                 ])


# > python -m pytest
