
from unittest import TestCase
from unittest.mock import patch
from src.utils.core import get_renewal_reminder_date
from src.services.subscriptions import SubscriptionsService

from io import StringIO


class DoremiTests(TestCase):

    def test_get_renewal_reminder_date(self):
        future_date = get_renewal_reminder_date("02-04-2020", 2)
        self.assertEqual(future_date, "23-05-2020")
        self.assertIsInstance(future_date, str, "Future date is expected to be string")

    def test_start_subscription(self):
        s = SubscriptionsService()
        s.start_subscription("02-04-2020")
        self.assertEqual(s.get_start_subscription(), "02-04-2020")

    def test_add_subscription_without_date(self):
        s = SubscriptionsService()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            s.add_subscription("MUSIC", "FREE")
            self.assertEqual(fake_out.getvalue(), "ADD_SUBSCRIPTION_FAILED\tINVALID_DATE\n")
    #
    # def test_add_duplicate_subscription(self):
    #     s = SubscriptionsService()
    #     with patch('sys.stdout', new=StringIO()) as fake_out:
    #         s.start_subscription("02-04-2020")
    #         s.add_topup("MUSIC", "FREE")
    #         s.add_topup("MUSIC", "FREE")
    #         self.assertEqual(fake_out.getvalue(), "ADD_SUBSCRIPTION_FAILED\tDUPLICATE_CATEGORY\n")
