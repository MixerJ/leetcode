import unittest

from sample.programs.number_7 import Solution


class TestNumber7(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_success(self):
        self.assertEqual(self.solution.reverse(312), 213)
        self.assertEqual(self.solution.reverse(-312), -213)
        self.assertEqual(self.solution.reverse(
            100000000000000009), 0)


if __name__ == '__main__':
    unittest.main()
