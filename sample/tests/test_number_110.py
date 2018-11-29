import unittest

from sample.programs.number_104 import Solution


class TestNumber104(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_success(self):
        self.assertTrue(self.solution.isBalanced([3, 9, 20, null, null, 15, 7]))
        self.assertFalse(self.solution.isBalanced([1, 2, 2, 3, 3, null, null, 4, 4]))

if __name__ == '__main__':
    unittest.main()
