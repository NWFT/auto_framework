# test_cases/test_login.py
import time

import pytest
from test_cases.base_case import BaseCase
from pages_object.login_page import LoginPage
from pages_object.home_page import HomePage
from test_data.login_data import positive_cases, native_cases
from test_data import urls_for_all


# @pytest.mark.usefixtures("driver")
class TestLogin(BaseCase):
    name = 'Login function'

    @pytest.mark.smoke
    # @pytest.mark.parametrize('case', positive_cases)
    def test_login_success(self, driver):
        """test login successful"""
        # 1. open login page
        # driver.get(urls_for_all.LOGIN_URL)
        driver.get("https://www.google.com")

        # 2. login action
        lp = LoginPage(driver)
        lp.get_error_tip_msg()
        time.sleep(2)
        print("##########################", lp)

        # lp.login(**case['data'])
        # # 3. assert login ok
        # hp = HomePage(driver)
        # assert hp.is_exit_exist()
        # # 4. logout
        # hp.logout()
        # # 5. access login page again
        # lp.load_page_with_url(urls_for_all.LOGIN_URL)
        # # 6. assert username saved
        # if case['data']['remember']:
        #     # assert username
        #     assert lp.get_saved_username_value() == case['data']['username']
        # else:
        #     # assert not saved
        #     assert not lp.get_saved_username_value()

    @pytest.mark.regression
    @pytest.mark.parametrize('case', native_cases)
    def test_login_error(self, driver, case):
        """login failed"""
        # 1. open login page
        driver.get(urls_for_all.LOGIN_URL)
        # 2. login actions
        lp = LoginPage(driver)
        lp.login(**case['data'])
        # 3. 断言
        assert case['error_msg'] == lp.get_error_tip_msg()

