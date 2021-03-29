import os
import importlib
import unittest

SRC_PATH = os.path.join(os.getcwd(), '..', 'src')


def load_test_cases():
    test_cases = []
    
    for module in os.listdir(SRC_PATH):
        if os.path.isdir(os.path.join(SRC_PATH, module)) and module != '__pycache__':
            test_cases.append(getattr(importlib.import_module(f'src.{module}.test'), 'SolutionTestCase'))
    
    return test_cases


def main():
    loader = unittest.TestLoader()
    
    test_cases = load_test_cases()
    suites_list = []
    for test_class in test_cases:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)
    
    big_suite = unittest.TestSuite(suites_list)
    
    unittest.TextTestRunner().run(big_suite)


if __name__ == '__main__':
    main()
