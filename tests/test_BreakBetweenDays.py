import unittest
import pandas as pd
import sys
sys.path.append("..")

from Validator import Validator


class TestBreakBetweenDays(unittest.TestCase):

    def setUp(self):
        TEST_INPUT_DIR = './test_data/'
        test_file_name_proper_break = 'test_proper_break.csv'
        test_file_name_too_short_break = 'test_too_short_break.csv'
        test_file_name_min_break = 'test_min_break.csv'

        try:
            data_proper_break = pd.read_csv(TEST_INPUT_DIR + test_file_name_proper_break,
                               sep=',',
                               header=0)
            data_too_short_break = pd.read_csv(TEST_INPUT_DIR + test_file_name_too_short_break,
                                    sep=',',
                                    header=0)
            data_min_break = pd.read_csv(TEST_INPUT_DIR + test_file_name_min_break,
                                               sep=',',
                                               header=0)

        except IOError:
            print('cannot open file')

        self.d_proper = data_proper_break
        self.d_too_short = data_too_short_break
        self.d_min = data_min_break

    def test_check_if_too_short_break_between_days_1(self):
        validator_proper = Validator(self.d_proper)
        self.assertFalse(validator_proper.check_if_too_short_break_between_days())

    def test_check_if_too_short_break_between_days_2(self):
        validator_short = Validator(self.d_too_short)
        self.assertTrue(validator_short.check_if_too_short_break_between_days())

    def test_check_if_too_short_break_between_days_3(self):
        validator_min = Validator(self.d_min)
        self.assertFalse(validator_min.check_if_too_short_break_between_days())


if __name__ == '__main__':
    unittest.main()
