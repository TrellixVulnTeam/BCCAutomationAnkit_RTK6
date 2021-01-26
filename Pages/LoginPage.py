from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from Config.config import TestData


class LoginPage(BasePage):
    EMAIL = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN = (By.ID, "submit")
    SIGNUP_LINK = (By.ID, "new_account")

    """constructor of the page class"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """Page actions"""

    def get_login_page_title(self, title):
        return self.get_title()

    def is_create_user_exist(self):
        return self.is_visible(self.SIGNUP_LINK)

    """Login to Application"""

    def do_login(self, username, password):
        self.do_send_keys(self.EMAIL, username)
        self.do_click(self.LOGIN)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN)


