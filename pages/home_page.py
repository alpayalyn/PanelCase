from selenium.webdriver.common.by import By
from base.base_page import BaseClass


class GachaponHome:
    """

        Navigates users to the Campaign Page.

    """

    MENU_CLICKED = (By.CSS_SELECTOR, ".qa-icon i-c-4") # 27
    OPTIMIZE_CLICKED = (By.CSS_SELECTOR, ".i-c-4 mr-2") # 0
    INSTORY_CLICKED = (By.CSS_SELECTOR, ".h-7-s d-f a-i-c px-4 py-2 ml-5") # 29
    

    def __init__(self, driver):
        self.driver = driver
        self.methods = BaseClass(self.driver)

    def navigating_to_in_story_page(self):
        """Website navigates to the campaign page."""
        self.methods.click_the_element(self.MENU_CLICKED, 27)
        self.methods.click_the_element(self.OPTIMIZE_CLICKED, 0)
        self.methods.click_the_element(self.INSTORY_CLICKED, 29)

    def checking_details(self):

