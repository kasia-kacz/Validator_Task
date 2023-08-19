import unittest
import pandas as pd

from Validator import Validator


class TestSumHigherThenNorm(unittest.TestCase):

    def setUp(self):
        TEST_INPUT_DIR = './test_data/'
        test_file_name_less = 'test_norm_less.csv'
        test_file_name_equal = 'test_norm_equal.csv'
        test_file_name_higher = 'test_norm_higher.csv'

        try:
            data_less = pd.read_csv(TEST_INPUT_DIR + test_file_name_less,
                               sep=',',
                               header=0)
            data_equal = pd.read_csv(TEST_INPUT_DIR + test_file_name_equal,
                                    sep=',',
                                    header=0)
            data_higher = pd.read_csv(TEST_INPUT_DIR + test_file_name_higher,
                                    sep=',',
                                    header=0)
        except IOError:
            print('cannot open file')
        self.d_less = data_less
        self.d_equal = data_equal
        self.d_higher = data_higher

    def test_check_if_sum_of_hours_higher_then_norm_1(self):
        validator_less = Validator(self.d_less)
        self.assertFalse(validator_less.check_if_sum_of_hours_higher_then_norm())

    def test_check_if_sum_of_hours_higher_then_norm_2(self):
        validator_equal = Validator(self.d_equal)
        self.assertFalse(validator_equal.check_if_sum_of_hours_higher_then_norm())

    def test_check_if_sum_of_hours_higher_then_norm_3(self):
        validator_higher = Validator(self.d_higher)
        self.assertTrue(validator_higher.check_if_sum_of_hours_higher_then_norm())


if __name__ == '__main__':
    unittest.main()
