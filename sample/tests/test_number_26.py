import unittest

from sample.programs.number_26 import Solution


class TestNumber26(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_success(self):
        self.assertEqual(self.solution.removeDuplicates([1, 1, 2]), 2)
        self.assertEqual(self.solution.removeDuplicates(
            [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]), 5)


if __name__ == '__main__':
    unittest.main()
