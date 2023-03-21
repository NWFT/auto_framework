from pagee_elements_locator.login_page_locator import LoginPageLocators as loc
from pages_object.base_page import BasePage


class LoginPage(BasePage):
    name = "Login_Page"

    def login(self, user, password):
        """
        Login page's login action, input user/pwd and click to submit
        :param user: username
        :param password: password
        :return: None
        """
        self.input_text(loc.username_loc, "Login_input_username", user)
        self.input_text(loc.password_loc, "Login_input_password", password)
        self.click_element(loc.submit_loc, "Login_click_submit")

    def get_error_msg_from_login_area(self):
        """
        get error messages when login failed.
        :return: text
        """
        return self.get_text(loc.login_failed_error_msg_loc, "Login_Get_error_msg")