import unittest

from sample.programs.number_100 import Solution


class TestNumber100(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_success(self):
        self.assertTrue(self.solution.isSameTree([1, 2, 3],  [1, 2, 3]))
        self.assertFalse(self.solution.isSameTree([1, 2],  [1, None, 3]))
        self.assertFalse(self.solution.isSameTree([1, 2, 1],  [1, 1, 2]))


if __name__ == '__main__':
    unittest.main()
