import unittest
import pandas as pd

from Validator import Validator


class TestCountWorkingNorm(unittest.TestCase):

    def setUp(self):
        TEST_INPUT_DIR = './test_data/'
        test_file_name_31 = 'test_norm_31_days.csv'
        test_file_name_30 = 'test_norm_30_days.csv'

        try:
            data_31_days = pd.read_csv(TEST_INPUT_DIR + test_file_name_31,
                               sep=',',
                               header=0)
            data_30_days = pd.read_csv(TEST_INPUT_DIR + test_file_name_30,
                                    sep=',',
                                    header=0)

        except IOError:
            print('cannot open file')

        self.d_31 = data_31_days
        self.d_30 = data_30_days

    def test_count_working_norm_1(self):
        validator_31 = Validator(self.d_31)
        self.assertEqual(validator_31.count_working_norm(), 216)

    def test_count_working_norm_2(self):
        validator_30 = Validator(self.d_30)
        self.assertEqual(validator_30.count_working_norm(), 200)


if __name__ == '__main__':
    unittest.main()
