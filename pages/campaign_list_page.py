import time

from selenium.webdriver.common.by import By
from base.base_page import BaseClass


class GachaponCampaignListPage:
    """

        Navigates users to the Campaign Page.

    """

    WAITING_ELEMENT_CAMPAIGN_NAME = (By.CSS_SELECTOR, ".in-data-table-wrapper__data-information")
    CREATE_CAMPAIGN = (By.CSS_SELECTOR, ".in-button-wrapper_create-default")  #0
    CAMPAIGN_NAME_TARGET = (By.CSS_SELECTOR, ".in-text-input-wrapper__input")  # 2
    CAMPAIGN_NAME_DATA = "SEL-001-AAA34"
    CREATE_TEST = (By.CSS_SELECTOR, ".in-button-wrapper")  # 8
    SEARCH_FILTER = (By.CSS_SELECTOR, ".in-text-input-wrapper__input") #1
    DETAILS = (By.CSS_SELECTOR, ".ml-1") #6
    CAMPAIGN_STATUS_TEXT = (By.CSS_SELECTOR, ".d-i-b") #11
    CAMPAIGN_SEGMENTATION = (By.CSS_SELECTOR, ".t-c-3") #9
    CAMPAIGN_RULES = (By.CSS_SELECTOR, ".personalization-rule-0") #0
    CAMPAIGN_VARIATION = (By.CSS_SELECTOR, ".tooltip") #1
    CAMPAIGN_GOALS_FIRST = (By.CSS_SELECTOR, ".personalization-goal-main") #0
    CAMPAIGN_GOALS_SECOND = (By.CSS_SELECTOR, ".personalization-goal-0") #0
    CAMPAIGN_PRIORITY_TEXT = (By.CSS_SELECTOR, ".t-a-r") #1
    NOTES = (By.CSS_SELECTOR, ".personalization-note") #0

    def __init__(self, driver):
        self.driver = driver
        self.methods = BaseClass(self.driver)

    def creating_new_campaign(self):
        """Website navigates to the campaign page."""
        self.methods.wait_for_element(self.WAITING_ELEMENT_CAMPAIGN_NAME, 0)
        self.methods.click_the_element(self.CREATE_CAMPAIGN, 0)
        self.methods.wait_for_element(self.CAMPAIGN_NAME_TARGET, 2).send_keys(self.CAMPAIGN_NAME_DATA)
        self.methods.click_the_element(self.CREATE_TEST, 8)

    def checking_campaign_status(self):
        time.sleep(5)
        return self.methods.get_text(self.CAMPAIGN_STATUS_TEXT, 11)

    def checking_necessary_data_segments(self):
        time.sleep(5)
        self.methods.get_text(self.CAMPAIGN_SEGMENTATION, 9)

    def checking_necessary_data_rules(self):
        return self.methods.get_text(self.CAMPAIGN_RULES, 0)

    def checking_necessary_data_variants(self):
        return self.methods.get_text(self.CAMPAIGN_VARIATION, 1)

    def checking_necessary_data_goals_first(self):
        self.methods.get_text(self.CAMPAIGN_GOALS_FIRST, 0)

    def checking_necessary_data_goals_second(self):
        self.methods.get_text(self.CAMPAIGN_GOALS_SECOND, 0)

    def checking_necessary_data_notes(self):
        self.methods.get_text(self.NOTES, 0)

    def checking_necessary_data_priority(self):
        return self.methods.get_text(self.CAMPAIGN_PRIORITY_TEXT, 1)
