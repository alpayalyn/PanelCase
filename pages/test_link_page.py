from selenium.webdriver.common.by import By
from base.base_page import BaseClass


class GachaponCampaignPage:
    """

        Navigates users to the Campaign Page.

    """

    CLICK_TEST_LINK = (By.CSS_SELECTOR, ".ml-1") #4

    def __init__(self, driver):
        self.driver = driver
        self.methods = BaseClass(self.driver)

    def creating_new_campaign(self):
        """Website navigates to the campaign page."""
        self.methods.click_the_element(self.CLICK_TEST_LINK, 4)
