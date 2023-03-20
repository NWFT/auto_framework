from base.base_actions import BaseAction
from .constants import index_url,HOME_ELEMENTS,LOGIN_ELEMENTS


class HomepageActions(BaseAction):
    def __init__(self, driver):
        super().__init__(driver)

    def go_to_homepage(self):
        self.driver.get(index_url)

    def click_to_login_page(self):
        self.click_element(HOME_ELEMENTS['login_btn'])

    def click_to_logout(self):
        self.click_element(HOME_ELEMENTS['logout_btn'])

