from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC



class BaseAction(object):
    def __init__(self, driver):
        self.driver = driver
        # self.driver.current_url()

    # find element, return object
    def find_element(self, loc, webelement=None):
        """
        loc : (By.ID, "xxx")
        with 'loc', get element, return element object
        :param loc:
        :param webelement:
        :return:
        """
        if isinstance(webelement, WebElement):
            # if webelement, find element under the element
            # WebElement.find_element(By.class, value), sub-element
            return webelement.find_element(loc[0], loc[1])

        # from selenium.webdriver.common.by import By
        # from selenium.import webdriver
        # driver = webdriver.Chrome()
        # driver.find_element(By.xxx, value)
        return self.driver.find_element(loc[0],loc[1])

    # click element
    def click_element(self, loc):
        # click action
        obj = self.find_element(loc)
        obj.click()

    # input content
    def input_element_content(self, loc, content):
        # input contents
        obj = self.find_element(loc)
        obj.clear()
        obj.send_keys(content)

    # get content
    def get_element_content(self, loc):
        obj = self.find_element(loc)
        return obj.text

    # get current URL
    @property
    def current_url(self):
        # return current url
        return self.driver.current_url

