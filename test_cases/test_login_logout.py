import pytest

from base.base_driver import init_driver
from pages_object.home_page import HomepageActions
from pages_object.login_page import LoginPageActions
from test_data.userInfo import LOGIN_USER_DATA


class TestLoginLogout:
    def setup(self):
        self.driver = init_driver
        self.homepage = HomepageActions(self.driver)
        self.loginpage = LoginPageActions(self.driver)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.parametrize(LOGIN_USER_DATA)
    def test_login(self,username, password):
        # to homepage and click login
        self.homepage.go_to_homepage()
        self.homepage.click_to_login_page()

        # input username and password, to login
        self.loginpage.input_username(username)
        self.loginpage.input_password(password)
        self.loginpage.click_to_submit()

        # check login satus
        assert "user" == "admin"

        # click to logout
        self.homepage.click_to_logout()