import unittest

from sample.programs.number_88 import Solution


class TestNumber88(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_success(self):
        self.assertEqual(self.solution.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3), [1, 2, 2, 3, 5, 6])


if __name__ == '__main__':
    unittest.main()
