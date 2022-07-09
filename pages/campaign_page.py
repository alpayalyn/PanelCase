from selenium.webdriver.common.by import By
from base.base_page import BaseClass


class GachaponCampaignPage:
    """

        Navigates users to the Campaign Page.

    """

    CREATE_CAMPAIGN = (By.CSS_SELECTOR, ".in-button-wrapper")  # 3
    CAMPAIGN_NAME_TARGET = (By.CSS_SELECTOR, ".in-text-input-wrapper__input")  # 2
    CAMPAIGN_NAME_DATA = "SEL-001-AA"
    CREATE_TEST = (By.CSS_SELECTOR, ".in-button-wrapper")  # 8
    SAVE_CONTINUE_SEGMENTS = (By.CSS_SELECTOR, ".in-button-wrapper")  # 4
    PAGE_RULES_SELECT = (By.CSS_SELECTOR, ".b-c-4")  # 1
    SELECTING_RULE = (By.CSS_SELECTOR, ".o-h")  # 1
    SELECTING_PAGE_TYPE = (By.CSS_SELECTOR, ".option__2")  # 2
    SAVE_CONTINUE_RULES = (By.CSS_SELECTOR, ".in-button-wrapper")  # 10
    ADD_NEW_VARIATION = (By.CSS_SELECTOR, ".in-button-wrapper")  # 3
    JUMP_TO_LAUNCH = (By.CSS_SELECTOR, ".in-steps-wrapper__steps")  # 4
    SELECTING_LANGUAGE_SECTION = (By.CSS_SELECTOR, ".o-h")  # 1
    ALL_LANGUAGES_SELECTION = (By.CSS_SELECTOR, ".option__0")  # 2
    START_DATE_SCHEDULE_SELECTION = (By.CSS_SELECTOR, ".vue-daterange-picker")  # 0
    START_DATE_DATE_SELECTION = (By.CSS_SELECTOR, ".weekend")  # 5
    START_TIME_SCHEDULE_SELECTION = (By.CSS_SELECTOR, ".in-text-input-wrapper__input")  # 3
    START_TIME_SELECTION = (By.CSS_SELECTOR, ".option__0")  # 3
    NEVER_ENDS = (By.CSS_SELECTOR, ".in-radio-button-wrapper__label")  # 0
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
    ACTIVATION_STATUS_SELECTION = (By.CSS_SELECTOR, ".in-radio-button-wrapper__label")  # 6
    NOTES_AREA_SELECTION = (By.CSS_SELECTOR, ".in-form-item")  # 16
    NOTES_AREA_DATA = "Testing for Automation RoadMap"
    LAUNCH_SELECTION = (By.CSS_SELECTOR, ".in-button-wrapper") #8

    def __init__(self, driver):
        self.driver = driver
        self.methods = BaseClass(self.driver)

    def creating_new_campaign_before_variant(self):
        """Website navigates to the campaign page."""
        self.methods.click_the_element(self.CREATE_CAMPAIGN, 3)
        self.methods.wait_for_element(self.CAMPAIGN_NAME_TARGET, 2).send_keys(self.CAMPAIGN_NAME_DATA)
        self.methods.click_the_element(self.CREATE_TEST, 8)
        self.methods.click_the_element(self.SAVE_CONTINUE_SEGMENTS, 4)
        self.methods.click_the_element(self.PAGE_RULES_SELECT, 1)
        self.methods.click_the_element(self.SELECTING_RULE, 1)
        self.methods.click_the_element(self.SELECTING_PAGE_TYPE, 2)
        self.methods.click_the_element(self.SAVE_CONTINUE_RULES, 10)
        self.methods.click_the_element(self.ADD_NEW_VARIATION, 3)

    def creating_new_campaign_after_variant(self):
        self.methods.click_the_element(self.JUMP_TO_LAUNCH, 4)
        self.methods.click_the_element(self.SELECTING_LANGUAGE_SECTION, 1)
        self.methods.click_the_element(self.ALL_LANGUAGES_SELECTION, 2)
        self.methods.click_the_element(self.START_DATE_SCHEDULE_SELECTION, 0)
        self.methods.click_the_element(self.START_DATE_DATE_SELECTION, 5)
        self.methods.click_the_element(self.START_TIME_SCHEDULE_SELECTION, 3)
        self.methods.click_the_element(self.START_TIME_SELECTION, 3)
        self.methods.click_the_element(self.NEVER_ENDS, 0)
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
        self.methods.click_the_element(self.LAUNCH_SELECTION, 8)
