import unittest
import pandas as pd

from Validator import Validator


class TestWorkOnSunday(unittest.TestCase):

    def setUp(self):
        TEST_INPUT_DIR = './test_data/'
        test_file_name_without_sunday = 'test_norm_less.csv'
        test_file_name_with_sunday = 'test_norm_higher.csv'

        try:
            data_without_sunday = pd.read_csv(TEST_INPUT_DIR + test_file_name_without_sunday,
                               sep=',',
                               header=0)
            data_with_sunday = pd.read_csv(TEST_INPUT_DIR + test_file_name_with_sunday,
                                    sep=',',
                                    header=0)

        except IOError:
            print('cannot open file')
        self.d_without_sunday = data_without_sunday
        self.d_with_sunday = data_with_sunday

    def test_check_if_work_on_sunday_1(self):
        validator_without = Validator(self.d_without_sunday)
        self.assertFalse(validator_without.check_if_work_on_sunday())

    def test_check_if_work_on_sunday_2(self):
        validator_with = Validator(self.d_with_sunday)
        self.assertTrue(validator_with.check_if_work_on_sunday())


if __name__ == '__main__':
    unittest.main()
