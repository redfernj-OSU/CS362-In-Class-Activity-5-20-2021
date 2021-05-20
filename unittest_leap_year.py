import jacob_redfern_hw3_error_checked
import unittest

class leapYearTest(unittest.TestCase):

    def test_true_year(self):
        self.assertTrue(jacob_redfern_hw3_error_checked.leap_check(2016))

    def test_false_year(self):
        self.assertFalse(jacob_redfern_hw3_error_checked.leap_check(2021))

    def test_valid_year_neg(self):
        self.assertFalse(jacob_redfern_hw3_error_checked.verify_year(-5))

    def test_valid_year_pos(self):
        self.assertTrue(jacob_redfern_hw3_error_checked.verify_year(5))

    def test_valid_year_str(self):
        self.assertFalse(jacob_redfern_hw3_error_checked.verify_year("str"))

if __name__ == '__main__':
    unittest.main()
