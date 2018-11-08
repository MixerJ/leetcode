import unittest

from sample.programs.number_20 import Solution


class TestNumber14(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_success(self):
        self.assertTrue(self.solution.isValid(
            ''))
        self.assertTrue(self.solution.isValid(
            '()'))
        self.assertTrue(self.solution.isValid(
            '()[]{}'))
        self.assertFalse(self.solution.isValid(
            '(]'))
        self.assertFalse(self.solution.isValid(
            '([)]'))
        self.assertTrue(self.solution.isValid(
            '{[]}'))

        self.assertTrue(self.solution.stackCheckIsValid(
            ''))
        self.assertTrue(self.solution.stackCheckIsValid(
            '()'))
        self.assertTrue(self.solution.stackCheckIsValid(
            '()[]{}'))
        self.assertFalse(self.solution.stackCheckIsValid(
            '(]'))
        self.assertFalse(self.solution.stackCheckIsValid(
            '([)]'))
        self.assertTrue(self.solution.stackCheckIsValid(
            '{[]}'))


if __name__ == '__main__':
    unittest.main()
