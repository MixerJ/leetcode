import unittest

from sample.programs.number_35 import Solution


class TestNumber35(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_success(self):
        self.assertEqual(self.solution.searchInsert([1, 3, 5, 6], 5), 2)
        self.assertEqual(self.solution.searchInsert(
            [1, 3, 5, 6], 2), 1)
        self.assertEqual(self.solution.searchInsert(
            [1, 3, 5, 6], 7), 4)
        self.assertEqual(self.solution.searchInsert(
            [1, 3, 5, 6], 0), 0)


if __name__ == '__main__':
    unittest.main()
