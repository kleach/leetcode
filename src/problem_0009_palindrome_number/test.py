import unittest
from .solution import Solution

solution = Solution()


class SolutionTestCase(unittest.TestCase):
    def test_1(self):
        self.assertTrue(solution.isPalindrome(121))
    
    def test_2(self):
        self.assertFalse(solution.isPalindrome(-121))
    
    def test_3(self):
        self.assertFalse(solution.isPalindrome(10))
    
    def test_4(self):
        self.assertFalse(solution.isPalindrome(-101))


if __name__ == '__main__':
    unittest.main()
