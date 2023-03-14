from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class BaseAction(object):
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, loc, webelement=None):
        """
        get element, return element object
        :param loc:
        :param webelement:
        :return:
        """
        if isinstance(webelement, WebElement):
            # if webelement, find element
            # WebElement.find_element(By.class, value)
            return webelement.find_element(loc[0],loc[1])

        # from selenium.webdriver.common.by import By
        # from selenium.import webdriver
        # driver = webdriver.Chrome()
        # driver.find_element(By.xxx, value)
        return self.driver.find_element(loc[0],loc[1])