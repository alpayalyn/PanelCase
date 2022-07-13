import unittest
from test.gachapon_setup import Setup


class TestRun(unittest.TestCase, Setup):
    """Test case is:

        1. Log in the panel, go to Web Instory
        2. Create Web Instory campaign
        3. Fill all steps till Launch step
        4. Change campaign's language, date&time, display settings, add priority, notes
        and launch campaign as Active.
        5. Go to do list and check campaign status is Active and added variation is present in Test link menu
        6. Open campaign's details and check all information that was filled during launch is present there
        7. Go to website with the test link of the campaign.
        8. Verify that campaign is visible (Storage and class existence control is enough)

    """

    def setUp(self):
        Setup.__init__(self)

    def test_gachapon(self):
        self.GachaponLogin.login_into_account()
        self.GachaponHome.navigating_to_in_story_page()
        self.GachaponCampaignListPage.creating_new_campaign()
        self.GachaponCampaignPage.customizing_campaign_rules_page_before_variant()
        self.GachaponInstory.creating_variant_design()
        self.GachaponCampaignPage.customizing_campaign_design_page_after_variant()
        self.GachaponCampaignPage.customizing_campaign_goals_page_after_variant()
        self.GachaponCampaignPage.customizing_campaign_launch_page_after_variant()
        status_panel = self.GachaponCampaignListPage.checking_campaign_status_panel()
        rules_panel = self.GachaponCampaignListPage.checking_necessary_data_rules_panel()
        variant_id_panel = self.GachaponCampaignListPage.checking_necessary_data_variants_panel()
        goals_first_panel = self.GachaponCampaignListPage.checking_necessary_data_goals_first_panel()
        goals_second_panel = self.GachaponCampaignListPage.checking_necessary_data_goals_second_panel()
        priority_panel = self.GachaponCampaignListPage.checking_necessary_data_priority_panel()
        notes_panel = self.GachaponCampaignListPage.checking_necessary_data_notes_panel()

        self.GachaponCampaignPage.customizing_campaign_launch_page_after_variant_completion()

        status = self.GachaponCampaignListPage.checking_campaign_status()
        assert status == status_panel, "Status doesn't match."
        rules = self.GachaponCampaignListPage.checking_necessary_data_rules()
        assert rules == rules_panel, "Rules doesn't match."
        variant_id = self.GachaponCampaignListPage.checking_necessary_data_variants()
        assert variant_id == variant_id_panel, "Variant ID doesn't match."
        goals_first = self.GachaponCampaignListPage.checking_necessary_data_goals_first()
        assert goals_first == goals_first_panel, "First Goal doesn't match."
        goals_second = self.GachaponCampaignListPage.checking_necessary_data_goals_second()
        assert goals_second == goals_second_panel, "Second Goal doesn't match."
        priority = self.GachaponCampaignListPage.checking_necessary_data_priority()
        assert priority == priority_panel, "Priority doesn't match."
        notes = self.GachaponCampaignListPage.checking_necessary_data_notes()
        assert notes == notes_panel, "Note doesn't match."

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
