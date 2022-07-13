from selenium.webdriver.common.by import By
from base.base_page import BaseClass


class GachaponLogin:
    """

        Logging into the account & filling the needed information.

    """

    EMAIL = (By.CSS_SELECTOR, ".in-text-input-wrapper__input") #0
    EMAIL_DATA = 'alpay.alin@useinsider.com'
    PASSWORD = (By.CSS_SELECTOR, ".in-text-input-wrapper__input") #1
    PASSWORD_DATA = ''
    LOGIN = (By.ID, 'login-button')

    def __init__(self, driver):
        self.driver = driver
        self.methods = BaseClass(self.driver)

    def login_into_account(self):
        """Logging into the account & filling the needed information."""
        self.methods.wait_for_element(self.EMAIL, 0).send_keys(self.EMAIL_DATA)
        self.methods.wait_for_element(self.PASSWORD, 1).send_keys(self.PASSWORD_DATA)
        self.methods.click_the_element(self.LOGIN, 0)
