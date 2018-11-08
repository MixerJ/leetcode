import unittest

from sample.programs.number_14 import Solution


class TestNumber14(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_success(self):
        self.assertEqual(self.solution.longestCommonPrefix(
            ["flower", "flow", "flight"]), 'fl')
        self.assertEqual(self.solution.longestCommonPrefix(
            ["dog", "racecar", "car"]), '')


if __name__ == '__main__':
    unittest.main()
