import unittest

from sample.programs.number_83 import Solution


class TestNumber83(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_success(self):
        self.assertEqual(self.solution.deleteDuplicates([1, 1, 2]), [1, 2])
        self.assertEqual(self.solution.deleteDuplicates([1, 1, 2, 3, 3]), [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
