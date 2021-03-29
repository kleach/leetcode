import unittest
from .solution import Solution

solution = Solution()


class SolutionTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
            solution.firstnode2list(
                solution.addTwoNumbers(
                    solution.list2firstnode([2, 4, 3]),
                    solution.list2firstnode([5, 6, 4])
                    ),
                ),
            [7, 0, 8]
            )

    def test_2(self):
        self.assertEqual(
            solution.firstnode2list(
                solution.addTwoNumbers(
                    solution.list2firstnode([0]),
                    solution.list2firstnode([0])
                    ),
                ),
            [0]
            )

    def test_3(self):
        self.assertEqual(
            solution.firstnode2list(
                solution.addTwoNumbers(
                    solution.list2firstnode([9, 9, 9, 9, 9, 9, 9]),
                    solution.list2firstnode([9, 9, 9, 9])
                    ),
                ),
            [8, 9, 9, 9, 0, 0, 0, 1]
            )


if __name__ == '__main__':
    unittest.main()
