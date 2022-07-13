import time

from selenium.webdriver.common.by import By
from base.base_page import BaseClass


class GachaponInstory:
    """

        Navigates users to the Campaign Page.

    """

    WAITING_ELEMENT_ACTION_BUILDER_FIRST = (By.CSS_SELECTOR, ".btn-preview")
    OVERLAY = (By.CSS_SELECTOR, ".overlay") #0
    TEMPLATE_SELECT = (By.CSS_SELECTOR, ".btn-select") #0
    SELECT_ELEMENT_POPUP = (By.CSS_SELECTOR, ".inline-select-notification-confirm") #0
    IFRAME_SELECTION = (By.ID, 'iframe-edit')
    SELECT_HEADER = (By.CSS_SELECTOR, ".wrap") #1
    INSERT_AFTER_ELEMENT = (By.CSS_SELECTOR, ".append-after") #0
    SAVE_VARIATION = (By.CSS_SELECTOR, ".btn-save") #0

    def __init__(self, driver):
        self.driver = driver
        self.methods = BaseClass(self.driver)

    def creating_variant_design(self):
        """Website navigates to the campaign page."""
        time.sleep(40)
        self.methods.wait_for_element(self.WAITING_ELEMENT_ACTION_BUILDER_FIRST, 1)
        self.methods.click_the_element(self.TEMPLATE_SELECT, 0)
        self.methods.click_the_element(self.SELECT_ELEMENT_POPUP, 0)
        with self.methods.switch_frame(self.IFRAME_SELECTION):
            time.sleep(5)
            self.methods.click_the_element(self.SELECT_HEADER, 1)
        self.methods.click_the_element(self.INSERT_AFTER_ELEMENT, 0)
        self.methods.click_the_element(self.SAVE_VARIATION, 0)
