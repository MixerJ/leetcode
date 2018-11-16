import unittest

from sample.programs.number_53 import Solution


class TestNumber53(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_success(self):
        self.assertEqual(self.solution.maxSubArray(
            [-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
        self.assertEqual(self.solution.maxSubArray(
            [-1]), -1)


if __name__ == '__main__':
    unittest.main()
