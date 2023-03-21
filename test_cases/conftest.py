import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from common.handler_log import get_logger
from pages_object.login_page import LoginPage
from test_data import urls_for_all
import settings

logger = get_logger(__name__,debug=True)
"""
fixture: scope, yield, return value
"""


@pytest.fixture(scope="class", name="driver")
def driver():
    """
    instance web driver, Login_page
    :return: driver
    """
    logger.info("======== class fixture, open browser =======")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(settings.IMPLICITLY_TIME)
    yield driver
    logger.info("======== class fixture, close browser =======")
    driver.quit()

#
# @pytest.fixture(scope="function", name="back_to_login_page")
# def back_to_login_page(init):
#     logger.info("======== function fixture, goto login page =======")
#     init.get(urls_for_all.LOGIN_URL)
#
#
# @pytest.fixture(scope="class", name="login")
# def init_global_login_driver(init):
#     """
#     instance web driver, Login_page, and login
#     after, close driver
#     :return: driver
#     """
#     # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     # driver.implicitly_wait(global_data.IMPLICITLY_WAIT_TIME)
#     # driver.get(global_data.LOGIN_URL)
#     # LoginPage(driver).login(normal_user["user"], normal_user["password"])
#     # yield driver
#     # driver.quit()
#     # user fixture's feature, use "init" fixture, delete overlapped codes.
#     logger.info("======== class fixture, login page, login with global normal user =======")
#     # LoginPage(init).login(normal_user["user"], normal_user["password"])
#     yield init
#
#
# @pytest.fixture(scope="function", name="back_home")
# def back_homepage(login):
#     logger.info("======== function fixture, goto home page =======")
#     login.get(urls_for_all.BASE_URL)