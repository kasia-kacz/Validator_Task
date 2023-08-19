from unittest import TestLoader, TestResult
from pathlib import Path


def run_tests():
    test_loader = TestLoader()
    test_result = TestResult()

    test_directory = str(Path(__file__).resolve().parent)
    test_suite = test_loader.discover(test_directory, pattern='test_*.py')
    test_suite.run(result=test_result)

    if test_result.wasSuccessful():
        print(test_result)
        exit(0)
    else:
        print(test_result)
        exit(-1)


if __name__ == '__main__':
    run_tests()
