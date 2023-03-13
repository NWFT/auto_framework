from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def init_driver():
    """
    init and return a Chrome web driver object
    :return: driver selenium.webdriver.ChromeDriver()
    """
    # create a option object
    option = webdriver.ChromeOptions()
    # add a headless option
    # option.add_argument("--headless")

    # create a driver object, install Chrome Driver with current Chrome browser
    web_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)

    # maximize window size
    web_driver.maximize_window()
    # implicitly wait time
    web_driver.implicitly_wait(20)

    return web_driver


if __name__ == '__main__':
    driver = init_driver()
    driver.get("http://www.google.com")

    driver.close()
