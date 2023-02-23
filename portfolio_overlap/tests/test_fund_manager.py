from unittest.case import TestCase

from src.services.fund_manager_impl import MutualFundManagerImpl


class FundManagerTest(TestCase):
    fms = MutualFundManagerImpl()

    def test_get_mutual_fund_by_name(self):
        mutual_fund = self.fms.find_mutual_fund_by_name("AXIS_BLUECHIP")
        self.assertEqual(mutual_fund.name, "AXIS_BLUECHIP")

    def test_get_stocks(self):
        stocks = self.fms.get_stocks("AXIS_BLUECHIP")
        self.assertIsInstance(stocks, list)

    def test_calculate_overlap(self):
        self.fms.calculate_overlap("AXIS_BLUECHIP", "MIRAE_ASSET_EMERGING_BLUECHIP")
