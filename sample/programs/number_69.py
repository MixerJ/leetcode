class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 牛顿法
        # if x <= 1:
        #     return x
        # r = x
        # while r > x / r:
        #     r = (r + x / r) // 2
        # return int(r)
        # 二分法
        if x == 1:
            return 1
        if x == 0:
            return 0
        l, r = 0, x-1
        while l <= r:
            mid = l + ((r - l) >> 2)
            if (mid * mid - x == 0):
                return mid
            elif (mid * mid - x > 0):
                r = mid - 1
            else:
                l = mid + 1
        return r
