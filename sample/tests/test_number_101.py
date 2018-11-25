import unittest

from sample.programs.number_101 import Solution


class TestNumber101(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_success(self):
        self.assertTrue(self.solution.isSameTree([1, 2, 2, 3, 4, 4, 3]))


if __name__ == '__main__':
    unittest.main()
