from base.base_actions import BaseAction
from .constants import login_url,LOGIN_ELEMENTS


class LoginPageActions(BaseAction):
    def __init__(self, driver):
        super().__init__(driver)

    def go_to_login_page(self):
        self.driver.get(login_url)

    def input_username(self, username):
        self.input_element_content(LOGIN_ELEMENTS['login_username'], username)

    def input_password(self, password):
        self.input_element_content(LOGIN_ELEMENTS['login_password'], password)

    def click_to_submit(self):
        self.click_element(LOGIN_ELEMENTS['login_btn'])

