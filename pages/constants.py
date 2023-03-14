
"""
All variables should be used in the project.
"""
from selenium.webdriver.common.by import By


# # URLs
# Homepage
index_url = "https://alex-info.ca"
# Login page
login_url = "https://alex-info.ca/login"
#


# # Elements
HOME_ELEMENTS = {
    # before login
    "login_btn": "(By.LINK_TEXT, 'login')",
    # after login
    'logged_info': "(By.CLASS_NAME, 'login_btn')",
    'logged_info_username': "(By.TAG_NAME, 'em')",
    'logout_btn': "(By.LINK_TEXT, 'logout')",
}

LOGIN_ELEMENTS = {
    "login_username": "(By.ID, 'username')",
    'login_password': "(By.ID, 'password')",
    "login_btn": "(By.CLASS_NAME, 'input_submit')",
}


if __name__ == '__main__':
    print(HOME_ELEMENTS['login_btn'])