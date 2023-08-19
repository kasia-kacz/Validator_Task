import unittest
import pandas as pd

from Validator import Validator


class TestSumOfOvertime(unittest.TestCase):

    def setUp(self):
        TEST_INPUT_DIR = './test_data/'
        test_file_name_no_overtime = 'test_no_overtime.csv'
        test_file_name_overtime_with_sundays = 'test_overtime_with_sundays.csv'
        test_file_name_overtime_without_sundays = 'test_overtime_without_sundays.csv'

        try:
            data_no_overtime = pd.read_csv(TEST_INPUT_DIR + test_file_name_no_overtime)
            data_without_sundays = pd.read_csv(TEST_INPUT_DIR + test_file_name_overtime_without_sundays)
            data_with_sundays = pd.read_csv(TEST_INPUT_DIR + test_file_name_overtime_with_sundays)

        except IOError:
            print('cannot open file')

        self.d_no_overtime = data_no_overtime
        self.d_without_sundays = data_without_sundays
        self.d_with_sundays = data_with_sundays

    def test_sum_of_overtime_1(self):
        validator_no_ot = Validator(self.d_no_overtime)
        self.assertEqual(validator_no_ot.count_sum_of_overtime(), 0)

    def test_sum_of_overtime_2(self):
        validator_without_sundays = Validator(self.d_without_sundays)
        self.assertEqual(validator_without_sundays.count_sum_of_overtime(), 4)

    def test_sum_of_overtime_3(self):
        validator_with_sundays = Validator(self.d_with_sundays)
        self.assertEqual(validator_with_sundays.count_sum_of_overtime(), 12)


if __name__ == '__main__':
    unittest.main()
