import unittest
from .solution import Solution

solution = Solution()


class SolutionTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
            solution.findMedianSortedArrays([1, 3], [2]),
            2.)
    
    def test_2(self):
        self.assertEqual(
            solution.findMedianSortedArrays([1, 2], [3, 4]),
            2.5)
    
    def test_3(self):
        self.assertEqual(
            solution.findMedianSortedArrays([0, 0], [0, 0]),
            0.)
    
    def test_4(self):
        self.assertEqual(
            solution.findMedianSortedArrays([], [1]),
            1.)
    
    def test_5(self):
        self.assertEqual(
            solution.findMedianSortedArrays([2], []),
            2.)


if __name__ == '__main__':
    unittest.main()
