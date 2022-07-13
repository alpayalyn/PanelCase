import time

from selenium.webdriver.common.by import By
from base.base_page import BaseClass


class GachaponCampaignPage:

    """

        Navigates users to the Campaign Page.

    """

    WAITING_ELEMENT_SEGMENTS_FIRST = (By.CSS_SELECTOR, ".fl-l.f-s-3.w-b-b-w") #0
    WAITING_ELEMENT_SEGMENTS_SECOND = (By.CSS_SELECTOR, ".in-link-wrapper__link_secondary")
    WAITING_ELEMENT_DESIGN_THIRD = (By.CSS_SELECTOR, ".in-text-input-wrapper__input_grey")
    WAITING_ELEMENT_RULES_FOURTH = (By.CSS_SELECTOR, ".page-behavior-rules.qa-page-behavior-rules") #0
    WAITING_ELEMENT_RULES_FIFTH = (By.CSS_SELECTOR, ".in-steps-wrapper__steps") #1
    WAITING_ELEMENT_DESIGN_SIXTH = (By.CSS_SELECTOR, ".in-button-wrapper_text-default") #2
    WAITING_ELEMENT_DESIGN_SEVENTH = (By.CSS_SELECTOR, ".in-steps-wrapper__steps") #3
    WAITING_ELEMENT_DESIGN_SEVENTH2 = (By.CSS_SELECTOR, ".in-text-input-wrapper__input_grey") #1
    WAITING_ELEMENT_DESIGN_SEVENTH3 = (By.CSS_SELECTOR, ".in-link-wrapper__link_secondary") #0
    WAITING_ELEMENT_GOALS_EIGHTH = (By.CSS_SELECTOR, ".in-button-wrapper_secondary-default") #0
    WAITING_ELEMENT_GOALS_NINTH = (By.CSS_SELECTOR, ".in-steps-wrapper__steps") #4
    WAITING_ELEMENT_LAUNCH_TENTH = (By.CSS_SELECTOR, ".in-steps-wrapper__steps") #1
    WAITING_ELEMENT_LAUNCH_ELEVENTH = (By.CSS_SELECTOR, ".in-radio-button-wrapper__label") #1
    SAVE_CONTINUE_SEGMENTS = (By.CSS_SELECTOR, ".in-button-wrapper")  # 4
    PAGE_RULES_SELECT = (By.CSS_SELECTOR, ".page-rules.qa-page-rules")  # 0
    PAGE_RULES_SELECTING_RULE = (By.CSS_SELECTOR, ".o-h")  # 1
    PAGE_RULES_SELECT_PAGE_TYPE = (By.CSS_SELECTOR, ".option__2")  # 2
    PAGE_RULES_SAVE_CONTINUE = (By.CSS_SELECTOR, ".in-button-wrapper_primary-default")  # 0
    DESIGN_ADD_NEW_VARIATION = (By.CSS_SELECTOR, ".in-button-wrapper_secondary-default")  # 0
    DESIGN_VARIATION_ID_DATA = (By.CSS_SELECTOR, ".t-c-2") #2
    DESIGN_SAVE_CONTINUE = (By.CSS_SELECTOR, ".in-button-wrapper_primary-default")  # 0
    GOALS_DATA_FIRST = (By.CSS_SELECTOR, ".t-c-2") #5
    GOALS_DATA_SECOND = (By.CSS_SELECTOR, ".t-c-2") #8
    GOALS_SAVE_CONTINUE = (By.CSS_SELECTOR, ".in-button-wrapper_primary-default") #0
    LAUNCH_SELECTING_LANGUAGE_SECTION = (By.CSS_SELECTOR, ".o-h")  # 1
    LAUNCH_ALL_LANGUAGES_SELECTION = (By.CSS_SELECTOR, ".option__0")  # 2
    LAUNCH_START_DATE_SCHEDULE_SELECTION = (By.CSS_SELECTOR, ".vue-daterange-picker")  # 0
    LAUNCH_START_DATE_DATE_SELECTION = (By.CSS_SELECTOR, ".weekend")  # 5
    LAUNCH_START_TIME_SCHEDULE_SELECTION = (By.CSS_SELECTOR, ".in-text-input-wrapper__input")  # 3
    LAUNCH_START_TIME_SELECTION = (By.CSS_SELECTOR, ".option__0")  # 3
    LAUNCH_NEVER_ENDS = (By.CSS_SELECTOR, ".in-radio-button-wrapper__label")  # 0
    DISPLAY_SETTINGS_SELECTION = (By.CSS_SELECTOR, ".qa-accordion")  # 0
    DISPLAY_SETTINGS_START_TIME_DISPLAY_HOURS_SCHEDULE_SELECTION = (By.CSS_SELECTOR, ".in-text-input-wrapper__input")#4
    DISPLAY_SETTINGS_START_TIME_SELECTION_DISPLAY_HOURS = (By.CSS_SELECTOR, ".option__1")  # 3
    DISPLAY_SETTINGS_END_TIME_DISPLAY_HOURS_SCHEDULE_SELECTION = (By.CSS_SELECTOR, ".in-text-input-wrapper__input")  # 5
    DISPLAY_SETTINGS_END_TIME_SELECTION_DISPLAY_HOURS = (By.CSS_SELECTOR, ".option__47")  # 3
    ADVANCED_SETTINGS_SELECTION = (By.CSS_SELECTOR, ".in-accordion-wrapper")  # 1
    ADVANCED_SETTINGS_CHECK_BOX_SELECTION_FIRST = (By.CSS_SELECTOR, ".in-check-box-wrapper__label")  # 0
    ADVANCED_SETTINGS_EVERY_DROP_DOWN_SELECTION = (By.CSS_SELECTOR, ".in-button-wrapper")  # 5
    ADVANCED_SETTINGS_EVERY_TIME_SELECTION = (By.CSS_SELECTOR, ".option__0")  # 7
    ADVANCED_SETTINGS_REPEAT_DROP_DOWN_SELECTION = (By.CSS_SELECTOR, ".in-button-wrapper.qa-button")  # 4
    ADVANCED_SETTINGS_REPEAT_TIME_SELECTION = (By.CSS_SELECTOR, ".option__1")  # 5
    ADVANCED_SETTINGS_EMAIL_SELECTION = (By.CSS_SELECTOR, "new-tag")  # 0
    ADVANCED_SETTINGS_EMAIL_DATA = "testing78@gmail.com"
    ADVANCED_SETTINGS_CHECK_BOX_SELECTION_SECOND = (By.CSS_SELECTOR, ".in-check-box-wrapper__label")  # 1
    ADVANCED_SETTINGS_PRIORITY_SELECTION = (By.CSS_SELECTOR, ".in-button-wrapper")  # 6
    ADVANCED_SETTINGS_PRIORITY_DROP_DOWN_SELECTION = (By.CSS_SELECTOR, ".option__0")  # 8
    ADVANCED_SETTINGS_PRIORITY_DATA = (By.CSS_SELECTOR, ".o-h") #6
    ACTIVATION_STATUS_SELECTION = (By.CSS_SELECTOR, ".in-radio-button-wrapper__label")  # 6
    NOTES_AREA_SELECTION = (By.CSS_SELECTOR, ".in-form-item")  # 16
    NOTES_AREA_DATA = "Testing for Automation RoadMap"
    STATUS_TEXT = (By.CSS_SELECTOR, ".in-radio-button-wrapper__label") #5
    RULES_TEXT = (By.CSS_SELECTOR, ".o-h") #1
    VARIATION_TEXT = (By.CSS_SELECTOR, ".t-c-2.d-i-b.f-w-600") #0
    GOALS_FIRST_TEXT = (By.CSS_SELECTOR, ".t-c-2") #5
    GOALS_SECOND_TEXT = (By.CSS_SELECTOR, ".t-c-2") #8
    PRIORITY_TEXT = (By.CSS_SELECTOR, ".o-h") #6
    LAUNCH_SELECTION = (By.CSS_SELECTOR, ".in-button-wrapper") #8

    def __init__(self, driver):
        self.driver = driver
        self.methods = BaseClass(self.driver)

    def customizing_campaign_rules_page_before_variant(self):
        """Website navigates to the campaign page."""
        self.methods.wait_for_element(self.WAITING_ELEMENT_SEGMENTS_FIRST, 0)
        self.methods.wait_for_element(self.WAITING_ELEMENT_SEGMENTS_SECOND, 0)
        self.methods.click_the_element(self.SAVE_CONTINUE_SEGMENTS, 4)
        self.methods.wait_for_element(self.WAITING_ELEMENT_SEGMENTS_SECOND, 0)
        self.methods.wait_for_element(self.WAITING_ELEMENT_RULES_FOURTH, 0)
        self.methods.wait_for_element(self.WAITING_ELEMENT_RULES_FIFTH, 2)
        self.methods.click_the_element(self.PAGE_RULES_SELECT, 0)
        self.methods.click_the_element(self.PAGE_RULES_SELECTING_RULE, 1)
        self.methods.click_the_element(self.PAGE_RULES_SELECT_PAGE_TYPE, 2)
        self.methods.click_the_element(self.PAGE_RULES_SAVE_CONTINUE, 0)
        self.methods.click_the_element(self.DESIGN_ADD_NEW_VARIATION, 0)

    def customizing_campaign_design_page_after_variant(self):
        self.methods.wait_for_element(self.WAITING_ELEMENT_DESIGN_SEVENTH2, 1)
        self.methods.wait_for_element(self.WAITING_ELEMENT_RULES_FIFTH, 1)
        self.methods.click_the_element(self.DESIGN_SAVE_CONTINUE, 0)

    def customizing_campaign_goals_page_after_variant(self):
        self.methods.wait_for_element(self.WAITING_ELEMENT_GOALS_EIGHTH, 0)
        self.methods.wait_for_element(self.WAITING_ELEMENT_GOALS_NINTH, 4)
        self.methods.click_the_element(self.GOALS_SAVE_CONTINUE, 0)

    def customizing_campaign_launch_page_after_variant(self):
        self.methods.wait_for_element(self.WAITING_ELEMENT_LAUNCH_TENTH, 3)
        self.methods.wait_for_element(self.WAITING_ELEMENT_LAUNCH_ELEVENTH, 1)
        self.methods.click_the_element(self.LAUNCH_SELECTING_LANGUAGE_SECTION, 1)
        self.methods.click_the_element(self.LAUNCH_ALL_LANGUAGES_SELECTION, 2)
        self.methods.click_the_element(self.LAUNCH_START_DATE_SCHEDULE_SELECTION, 0)
        self.methods.click_the_element(self.LAUNCH_START_DATE_DATE_SELECTION, 5)
        self.methods.click_the_element(self.LAUNCH_START_TIME_SCHEDULE_SELECTION, 3)
        self.methods.click_the_element(self.LAUNCH_START_TIME_SELECTION, 3)
        self.methods.click_the_element(self.LAUNCH_NEVER_ENDS, 0)
        self.methods.click_the_element(self.DISPLAY_SETTINGS_SELECTION, 0)
        self.methods.click_the_element(self.DISPLAY_SETTINGS_START_TIME_DISPLAY_HOURS_SCHEDULE_SELECTION, 4)
        self.methods.click_the_element(self.DISPLAY_SETTINGS_START_TIME_SELECTION_DISPLAY_HOURS, 3)
        self.methods.click_the_element(self.DISPLAY_SETTINGS_END_TIME_DISPLAY_HOURS_SCHEDULE_SELECTION, 5)
        self.methods.click_the_element(self.DISPLAY_SETTINGS_END_TIME_SELECTION_DISPLAY_HOURS, 3)
        self.methods.click_the_element(self.ADVANCED_SETTINGS_SELECTION, 1)
        self.methods.click_the_element(self.ADVANCED_SETTINGS_CHECK_BOX_SELECTION_FIRST, 0)
        self.methods.click_the_element(self.ADVANCED_SETTINGS_EVERY_DROP_DOWN_SELECTION, 5)
        self.methods.click_the_element(self.ADVANCED_SETTINGS_EVERY_TIME_SELECTION, 7)
        self.methods.click_the_element(self.ADVANCED_SETTINGS_REPEAT_DROP_DOWN_SELECTION, 4)
        self.methods.click_the_element(self.ADVANCED_SETTINGS_REPEAT_TIME_SELECTION, 5)
        self.methods.wait_for_element(self.ADVANCED_SETTINGS_EMAIL_SELECTION, 2). \
            send_keys(self.ADVANCED_SETTINGS_EMAIL_DATA)
        self.methods.click_the_element(self.ADVANCED_SETTINGS_CHECK_BOX_SELECTION_SECOND, 1)
        self.methods.click_the_element(self.ADVANCED_SETTINGS_PRIORITY_SELECTION, 6)
        self.methods.click_the_element(self.ADVANCED_SETTINGS_PRIORITY_DROP_DOWN_SELECTION, 8)
        self.methods.click_the_element(self.ACTIVATION_STATUS_SELECTION, 6)
        self.methods.wait_for_element(self.NOTES_AREA_SELECTION, 16).send_keys(self.NOTES_AREA_DATA)

    def checking_campaign_status_panel(self):
        time.sleep(5)
        return self.methods.get_text(self.STATUS_TEXT, 5)

    def checking_necessary_data_rules_panel(self):
        time.sleep(5)
        return self.methods.get_text(self.RULES_TEXT, 1)

    def checking_necessary_data_variants_panel(self):
        time.sleep(5)
        return self.methods.get_text(self.VARIATION_TEXT, 0)

    def checking_necessary_data_goals_first_panel(self):
        time.sleep(5)
        return self.methods.get_text(self.GOALS_FIRST_TEXT, 5)

    def checking_necessary_data_goals_second_panel(self):
        time.sleep(5)
        return self.methods.get_text(self.GOALS_SECOND_TEXT, 8)

    def checking_necessary_data_priority_panel(self):
        time.sleep(5)
        return self.methods.get_text(self.PRIORITY_TEXT, 6)

    def customizing_campaign_launch_page_after_variant_completion(self):
        time.sleep(5)
        self.methods.click_the_element(self.LAUNCH_SELECTION, 8)
