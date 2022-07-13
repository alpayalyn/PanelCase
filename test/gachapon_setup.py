from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from pages.login_page import GachaponLogin
from pages.home_page import GachaponHome
from pages.campaign_list_page import GachaponCampaignListPage
from pages.campaign_page import GachaponCampaignPage
from pages.instory_page import GachaponInstory


class Setup:
    """
    Customizations will be adjusted.

    """
    driver_location = "/usr/bin/chromedriver"
    binary_location = "/usr/bin/google-chrome"
    option = webdriver.ChromeOptions()
    option.binary_location = binary_location
    driver = webdriver.Chrome(executable_path=driver_location, options=option)
    driver.maximize_window()
    url = "https://seleniumautomation1.inone.useinsider.com/"
    GachaponLogin = GachaponLogin(driver)
    GachaponHome = GachaponHome(driver)
    GachaponCampaignListPage = GachaponCampaignListPage(driver)
    GachaponCampaignPage = GachaponCampaignPage(driver)
    GachaponInstory = GachaponInstory(driver)

    def __init__(self):
        self.wait = WebDriverWait(self.driver, 1500)
        """Driver has been started."""
        option = Options()
        # option.add_argument("--disable-infobars")
        option.add_argument("start-maximized")
        # option.add_argument("--disable-extensions")
        self.driver.get(self.url)
        self.wait = WebDriverWait(self.driver, 1500)


if __name__ == '__main__':
    Setup()
