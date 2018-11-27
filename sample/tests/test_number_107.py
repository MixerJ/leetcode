import unittest

from sample.programs.number_104 import Solution


class TestNumber104(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_success(self):
        self.assertEqual(self.solution.levelOrderBottom([3, 9, 20, None, None, 15, 7]), [
  [15,7],
  [9,20],
  [3]
])


if __name__ == '__main__':
    unittest.main()
