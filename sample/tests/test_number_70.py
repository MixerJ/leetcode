import unittest

from sample.programs.number_70 import Solution


class TestNumber70(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_success(self):
        self.assertEqual(self.solution.climbStairs(2), 2)
        self.assertEqual(self.solution.climbStairs(3), 3)


if __name__ == '__main__':
    unittest.main()
