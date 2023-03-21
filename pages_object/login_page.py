from pagee_elements_locator.login_page_locator import LoginPageLocators as loc
from pages_object.base_page import BasePage


class LoginPage(BasePage):
    name = "Login_Page"

    def login(self, user, password, remember=True):
        """
        Login page's login action, input user/pwd and click to submit
        :param user: username
        :param password: password
        :return: None
        """
        self.input_text(loc.username_loc, "Login_input_username", user)
        self.input_text(loc.password_loc, "Login_input_password", password)

        # for remember username in login page
        element = self.get_element(loc.remember_loc, "Login_remember_checkbox")
        if remember:
            if not element.is_selected():
                # click to select
                element.click()
        else:
            if element.is_selected():
                # click to de-select
                element.click()

        # click submit button
        self.click_element(loc.submit_loc, "Login_click_submit")

    def get_saved_username_value(self):
        pass

    def get_error_tip_msg(self):
        self.input_text(loc.search_input_loc, "TESTXXXXXXXXXXXXXX", "XXXXXXXX")

    def get_error_msg_from_login_area(self):
        """
        get error messages when login failed.
        :return: text
        """
        return self.get_text(loc.login_failed_error_msg_loc, "Login_Get_error_msg")