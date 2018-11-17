import unittest

from sample.programs.number_58 import Solution


class TestNumber58(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_success(self):
        self.assertEqual(self.solution.lengthOfLastWord(
            "Hello World"), 5)
        self.assertEqual(self.solution.lengthOfLastWord(
            "a "), 1)
        self.assertEqual(self.solution.lengthOfLastWord("b   a    "), 1)


if __name__ == '__main__':
    unittest.main()
