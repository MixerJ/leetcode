import unittest

from sample.programs.number_104 import Solution


class TestNumber104(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_success(self):
        self.assertEqual(self.solution.isBalanced([3, 9, 20, null, null, 15, 7]), 2)

if __name__ == '__main__':
    unittest.main()
