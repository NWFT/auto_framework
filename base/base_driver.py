from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

"""
# driver attributes and methods
driver.page_source
driver.title
driver.current_url
driver.get(URL)
driver.close() # close current page
driver.quit()  # close driver
driver.forward()    # page forward
driver.back()       # page back
driver.screen_shot(img_name)    # 
driver.refresh()    # page refresh
driver.set_window_position(300,200)
driver.set_window_size(1024,768)
driver.maximize_window()
"""
"""
# driver find elements
driver.find_element(By.xx, value)
# By.id/name/xpath/class_name/link_text/partial_link/tag_name/css
driver.find_elements(By.xx, value)
"""
"""
# elements attributes and methods
driver.find_element(By.xx, value).size
driver.find_element(By.xx, value).text  # All itself text and children text
driver.find_element(By.xx, value).get_attribute("xxx")
driver.find_element(By.xx, value).is_displayed()
driver.find_element(By.xx, value).is_enabled()
"""

"""
#   change TABs when open many windows
# 1) get all pages handles
current_windows = driver.window_handles
# 2) switch to expected TAB
driver.switch_to.window(current_windows[1])

# Opening first url
driver.get(url)
  
# Open a new window
driver.execute_script("window.open('');")
  
# Switch to the new window and open new URL
driver.switch_to.window(driver.window_handles[1])
driver.get(new_url)
  
# Closing new_url tab
driver.close()
  
# Switching to old tab
driver.switch_to.window(driver.window_handles[0])
"""

"""
#   handle cookies
cookies_dict = {cookie['name']:cookie['value'] for cookie in driver.get_cookies()}
driver.delete_all_cookies()
"""

"""
# wait
1) time.sleep()
2) Implicitly   driver.implicitly_wait(10)   # wait paged loading 
3) Explicitly   from selenium.webdriver.support.wait import WebDriverWait
                from selenium.webdriver.support import expected_conditions as EC
                try:
                    WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.ID, "xxx")))
                except:
                    assert "timeout"
"""


def init_driver():
    """
    init and return a Chrome web driver object
    :return: driver selenium.webdriver.ChromeDriver()
    """
    # create a option object
    option = webdriver.ChromeOptions()
    # add a headless option
    # option.add_argument("--headless")
    # option.add_argument("--disable-gpu")

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
