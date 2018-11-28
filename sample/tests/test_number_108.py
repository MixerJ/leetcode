import unittest

from sample.programs.number_104 import Solution


class TestNumber104(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_success(self):
        self.assertEqual(self.solution.sortedArrayToBST([-10, -3, 0, 5, 9]), [0, -3, 9, -10, None, 5])

if __name__ == '__main__':
    unittest.main()
