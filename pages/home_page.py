import time
from selenium.webdriver.common.by import By
from base.base_page import BaseClass


class GachaponHome:
    """

        Navigates users to the Campaign Page.

    """

    MENU_CLICKED = (By.CSS_SELECTOR, ".in-sidebar-wrapper__groups")  # 2 .in-sidebar-wrapper__groups
    OPTIMIZE_CLICKED = (By.CSS_SELECTOR, ".p-r")  # 10 .p-r
    INSTORY_CLICKED = (By.CSS_SELECTOR, ".h-7-s")  # 16 .h-7-s
    WAIT_ELEMENT_CHART = (By.CSS_SELECTOR, ".chartjs-render-monitor")
    WAIT_ELEMENT_SCHEDULE = (By.CSS_SELECTOR, ".vue-daterange-picker")

    def __init__(self, driver):
        self.driver = driver
        self.methods = BaseClass(self.driver)

    def navigating_to_in_story_page(self):
        """Website navigates to the campaign page."""
        self.methods.wait_for_element(self.WAIT_ELEMENT_CHART, 0)
        self.methods.wait_for_element(self.WAIT_ELEMENT_SCHEDULE, 0)
        self.methods.click_the_element(self.MENU_CLICKED, 2)
        self.methods.click_the_element(self.OPTIMIZE_CLICKED, 10)
        self.methods.click_the_element(self.INSTORY_CLICKED, 16)
