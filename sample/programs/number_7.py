class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        mark = 1 if x > 0 else -1
        x = abs(x)
        result = mark * int(str(x)[::-1])
        return result if result < 2**31-1 and result > -2**31 else 0
