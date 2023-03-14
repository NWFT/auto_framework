import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_open_browser():
    # create a option object
    option = webdriver.ChromeOptions()

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)

    # maximize window size
    driver.maximize_window()
    # implicitly wait time
    driver.implicitly_wait(10)

    driver.get("https://www.google.com")
    print(driver.current_url)

    driver.quit()


if __name__ == '__main__':
    file = os.path.basename(__file__)
    pytest.main(["-s", file])

