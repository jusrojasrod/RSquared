from datetime import date
import unittest
import os
import sys
_parent_dp = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
_src_dp = _parent_dp
sys.path.insert(0, _src_dp)

from RSquared.strategy import Strategy


class TestStrategy(unittest.TestCase):

    def setUp(self) -> None:
        self.test = Strategy()

    def test_factor_end_date(self):
        self.test.factors_end_date = date(2022, 1, 1)
        self.assertEqual(self.test.endFF_date, date(2022, 1, 1),
                         "Incorrect end date")

    def test_factor_start_date(self):
        self.test.factors_start_date = date(2022, 1, 1)
        self.assertEqual(self.test.startFF_date, date(2022, 1, 1),
                         "Incorrect start date")


if __name__ == '__main__':
    unittest.main()
