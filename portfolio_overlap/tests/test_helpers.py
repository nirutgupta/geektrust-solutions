from unittest.case import TestCase

from src.utils.helpers import limit_float_decimal_points


class HelpersTest(TestCase):
    test_value = 1.245
    limit = 2

    def test_limit_float_decimal_points(self):
        self.assertEqual(limit_float_decimal_points(self.test_value, self.limit), "1.25")
