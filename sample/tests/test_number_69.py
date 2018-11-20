import unittest

from sample.programs.number_69 import Solution


class TestNumber69(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_success(self):
        self.assertEqual(self.solution.mySqrt(
            4), 2)
        self.assertEqual(self.solution.mySqrt(
            8), 2)
        self.assertEqual(self.solution.mySqrt(
            5), 2)


if __name__ == '__main__':
    unittest.main()
