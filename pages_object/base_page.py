
"""
Why?
    1. log every step for traceability
    2. deduce duplicated codes
        a) wait element visible
        b) find element
        c) click()
        d) input()
        e) get text
        f) get attributes
        -------------------
        g) switch_window switch driver to the last open window handle
"""
import os
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

from common.handler_log import get_logger
# from web.TestData import global_data
import settings
screenshots_dir = os.path.join(settings.BASE_DIR, 'logs')


logger = get_logger(__name__)


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def load_page_with_url(self, url):
        logger.info(f"Open browser with {url}, Waiting for page loading.")
        self.driver.get(url)

    def wait_element_visible(self, locator, page_operation, **kwargs):
        """
        Wait element visible.
        :param locator: element locator, from PageElementsLocator
        :param page_operation: page? which page, eg., login_page, register_page
                            operation? click, input, get_text, get_attributes
        :param timeout: waiting timeout default=10s
        :param poll_frequency: poll frequency, default=0.5s
        :return: None
        """
        logger.info(f"With {page_operation}, Waiting for element {locator} visible.")
        # get explicitly wait time
        timeout = kwargs.get('timeout', settings.EXPLICITLY_TIME)
        # get poll frequency
        poll_frequency = kwargs.get("poll_frequency", settings.POLL_FREQUENCY)
        try:
            # record case execution time
            start = time.time()
            # waiting for element visibility
            WebDriverWait(self.driver, timeout, poll_frequency).until(EC.visibility_of_element_located(locator))
        except:
            # log error
            logger.exception(f"Waiting element timeout after {timeout}s.")
            # failed screenshot
            self.get_page_screenshot(page_operation)
            # set this case failed
            raise
        else:
            end = time.time()
            logger.info("Spent {:.3f} seconds, on waiting.".format(end-start))
            return self

    def wait_element_clickable(self, locator, page_operation, **kwargs):
        """
        Wait element to be clickable.
        :param locator: element locator, from PageElementsLocator
        :param page_operation: page? which page, eg., login_page, register_page
                            operation? click, input, get_text, get_attributes
        :param timeout: waiting timeout default=10s
        :param poll_frequency: poll frequency, default=0.5s
        :return: None
        """
        logger.info(f"With {page_operation}, Waiting for element {locator} clickable.")
        # get explicitly wait time
        timeout = kwargs.get('timeout', settings.EXPLICITLY_TIME)
        # get poll frequency
        poll_frequency = kwargs.get("poll_frequency", settings.POLL_FREQUENCY)
        try:
            start = time.time()
            WebDriverWait(self.driver, timeout, poll_frequency).until(EC.element_to_be_clickable(locator))
        except:
            # log error
            logger.exception(f"Waiting element timeout after {timeout}s.")
            # failed screenshot
            self.get_page_screenshot(page_operation)
            # set this case failed
            raise
        else:
            end = time.time()
            logger.info("Spent {:.3f} seconds, on waiting.".format(end-start))
            return self

    def wait_page_contains_element(self, locator, page_operation, **kwargs):
        """
        Wait page contains element.
        :param locator: element locator, from PageElementsLocator
        :param page_operation: page? which page, eg., login_page, register_page
                            operation? click, input, get_text, get_attributes
        :param timeout: waiting timeout default=10s
        :param poll_frequency: poll frequency, default=0.5s
        :return: None
        """
        logger.info(f"With {page_operation}, Waiting for page contains element {locator}.")
        # get explicitly wait time
        timeout = kwargs.get('timeout', settings.EXPLICITLY_TIME)
        # get poll frequency
        poll_frequency = kwargs.get("poll_frequency", settings.POLL_FREQUENCY)
        try:
            start = time.time()
            WebDriverWait(self.driver, timeout, poll_frequency).until(EC.presence_of_element_located(locator))
        except:
            # log error
            logger.exception(f"Waiting page contains element timeout after {timeout}s.")
            # failed screenshot
            self.get_page_screenshot(page_operation)
            # set this case failed
            raise
        else:
            end = time.time()
            logger.info("Spent {:.3f} seconds, on waiting.".format(end-start))

    def get_element(self, locator, page_operation, wait=None, **kwargs):
        """
        Get the element after visible or page contains.
        :param locator: element's locator
        :param page_operation: Note for log and screenshot
        :param timeout: wait time with default
        :param poll_frequency: poll frequency with default
        :param wait: if wait not Nne, check page contains the element or not; else check element visible.
        :return: None
        """
        logger.info(f"With {page_operation}, Finding element {locator}.")
        # get explicitly wait time
        timeout = kwargs.get('timeout', settings.EXPLICITLY_TIME)
        # get poll frequency
        poll_frequency = kwargs.get("poll_frequency", settings.POLL_FREQUENCY)

        # before get element, should check page contains, or element visible
        # if wait Not None, page should contains element
        # else visible, default is wait_element_visible
        if wait:
            self.wait_page_contains_element(locator, page_operation, timeout=timeout, poll_frequency=poll_frequency)
        else:
            self.wait_element_visible(locator, page_operation, timeout=timeout, poll_frequency=poll_frequency)

        try:
            ele = self.driver.find_element(*locator)
        except:
            # log error
            logger.exception("Finding element failed.")
            # failed screenshot
            self.get_page_screenshot(page_operation)
            # set this case filed
            raise
        else:
            return ele

    def click_element(self, locator, page_operation, **kwargs):
        """
        Click the element. find element before the click operation.
        :param locator: element's locator
        :param page_operation: Note for log and screenshot
        :param timeout: wait time with default
        :param poll_frequency: poll frequency with default
        :return: None
        """
        # get explicitly wait time
        timeout = kwargs.get('timeout', settings.EXPLICITLY_TIME)
        # get poll frequency
        poll_frequency = kwargs.get("poll_frequency", settings.POLL_FREQUENCY)

        # wait element, find element
        ele = self.get_element(locator, page_operation, timeout=timeout, poll_frequency=poll_frequency)
        # click element
        logger.info(f"With {page_operation}, Click element {locator}.")
        try:
            ele.click()
        except:
            # log error
            logger.exception("With {page_operation}, Click element {locator}. Click element failed.")
            # failed screenshot
            self.get_page_screenshot(page_operation)
            # set this case filed
            raise

    def input_text(self, locator, page_operation, value, **kwargs):
        """
        Input some text value in the locator.
        :param locator: element's locator
        :param page_operation: Note for log and screenshot
        :param value: input value
        :param timeout: wait time with default
        :param poll_frequency: poll frequency with default
        :return: None
        """
        # get explicitly wait time
        timeout = kwargs.get('timeout', settings.EXPLICITLY_TIME)
        # get poll frequency
        poll_frequency = kwargs.get("poll_frequency", settings.POLL_FREQUENCY)

        # wait element, find element
        ele = self.get_element(locator, page_operation, timeout=timeout, poll_frequency=poll_frequency)
        # input text
        logger.info(f"With {page_operation}, send text {value} to {locator}.")
        try:
            ele.clear()
            ele.send_keys(value)
        except:
            # log error
            logger.exception("With {page_operation}, send text {value} to {locator}, input text failed.")
            # failed screenshot
            self.get_page_screenshot(page_operation)
            # set this case filed
            raise

    def get_text(self, locator, page_operation, **kwargs):
        """
        Get the text of a locator.
        :param locator: element's locator
        :param page_operation: Note for log and screenshot
        :param timeout: wait time with default
        :param poll_frequency: poll frequency with default
        :return: locator's text
        """
        # get explicitly wait time
        timeout = kwargs.get('timeout', settings.EXPLICITLY_TIME)
        # get poll frequency
        poll_frequency = kwargs.get("poll_frequency", settings.POLL_FREQUENCY)

        # wait page contains element, find element
        ele = self.get_element(locator, page_operation, wait="contains", timeout=timeout, poll_frequency=poll_frequency)
        logger.info(f"With {page_operation}, Get element {locator} text.")
        try:
            text = ele.text
        except:
            # log error
            logger.exception("With {page_operation}, Get element {locator} text. Get element text failed.")
            # failed screenshot
            self.get_page_screenshot(page_operation)
            # set this case filed
            raise
        else:
            logger.info(f"Text value：{text}")
            return text

    def get_attribute(self, locator, page_operation, attr, **kwargs):
        """
        Give a locator and attr-name, get the attribute value.
        :param locator: element's locator
        :param page_operation: Note for log and screenshot
        :param attr: which attr-name's attribute value
        :param timeout: wait time with default
        :param poll_frequency: poll frequency with default
        :return: attribute
        """
        # get explicitly wait time
        timeout = kwargs.get('timeout', settings.EXPLICITLY_TIME)
        # get poll frequency
        poll_frequency = kwargs.get("poll_frequency", settings.POLL_FREQUENCY)

        # wait page contains element, find element
        ele = self.get_element(locator, page_operation, wait="contains", timeout=timeout, poll_frequency=poll_frequency)
        logger.info(f"With {page_operation}, Get element {locator} ({attr})'s attribute.")
        try:
            value = ele.get_attribute(attr)
        except:
            # log error
            logger.exception("With {page_operation}, Get element {locator} ({attr})'s attribute. \
                             Get element attribute failed.")
            # failed screenshot
            self.get_page_screenshot(page_operation)
            # set this case filed
            raise
        else:
            logger.info(f"Attribute value：{value}")
            return value

    def get_page_screenshot(self, page_operation):
        """
        Get current page screenshot when method used.
        :param page_operation: give page-name_operation-type, for name the png-file, the file saved in /output/screenshots
        :return: None
        """
        # image-name-format: {Page-name_Operation}_timestamp.png
        cur_time = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())
        file_path = os.path.join(screenshots_dir, "{}_{}.png".format(page_operation, cur_time))
        self.driver.save_screenshot(file_path)
        logger.info(f"Screenshot has been saved at: {file_path}")

    def switch_window(self, name="new"):
        """
        many windows used during test, switch between them.
        :param name: which window switch to, default is the last open one
        :return: None
        """
        # need time to open the new window
        logger.info("switch window begin.")
        time.sleep(1)
        # get all window handlers
        wins = self.driver.window_handles
        logger.info(f"all windows handlers: {wins}")
        # new, switch to the last open window
        if name == "new":
            # switch_to window/frame/
            logger.info(f"Change window to: {wins[-1]}")
            self.driver.switch_to.window(wins[-1])

    # use js to set readonly values
    def input_value_to_readonly_element(self, locator, page_operation, value):
        # get element
        logger.info("Input values to readonly element.")
        ele = self.get_element(locator, page_operation)
        # arguments[0] [1], parameters for js
        js_code = 'arguments[0].removeAttribute("readonly");' \
                  'arguments[0].value = arguments[1];'

        # js, values from outside to js code
        self.driver.execute_script(js_code, ele, value)

    # forward to homepage
    def page_go_to_homepage(self):
        logger.info("set driver go to home page.")
        self.driver.forward()

    # back to last page
    def page_back_to_last(self):
        logger.info("set driver back to the last page.")
        self.driver.back()

    # go to forward page
    def page_forward_to(self):
        logger.info("set driver forward to page.")
        self.driver.forward()

    # refresh current page
    def page_refresh(self):
        logger.info("set driver refresh current page.")
        self.driver.refresh()


if __name__ == '__main__':
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    base = BasePage(driver)

    base.load_page_with_url("https://www.google.com/")

    loc = (By.NAME, "q")
    # base.wait_element_visible(loc, "Login_Username")

    # get element
    # ele = base.get_element(loc, "Login_Username", wait="x")
    base.input_text(loc, "Homepage", "aaaaaa")
    # base.click_element((By.CLASS_NAME, "input_submit"), "Login_Username")
    #
    # print(base.get_text((By.XPATH, '//div[@id="error_info"]'),"Login_Submit-clicked"))
    # print(base.get_attribute((By.XPATH, '//div[@id="error_info"]'), "Login_Submit-clicked", "id"))
    time.sleep(2)
    logger.error("XXXXXX")
    driver.close()