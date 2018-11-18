import unittest

from sample.programs.number_66 import Solution


class TestNumber66(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_success(self):
        self.assertEqual(self.solution.plusOne(
            [1, 2, 3]), [1, 2, 4])
        self.assertEqual(self.solution.plusOne(
            [4, 3, 2, 1]), [4, 3, 2, 2])


if __name__ == '__main__':
    unittest.main()
