import unittest

from sample.programs.number_9 import Solution


class TestNumber9(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_success(self):
        self.assertFalse(self.solution.isPalindrome(123))
        self.assertTrue(self.solution.isPalindrome(121))
        self.assertFalse(self.solution.isPalindrome(-121))


if __name__ == '__main__':
    unittest.main()
