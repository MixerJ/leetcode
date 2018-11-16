class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        max_return = float('-inf')
        for i in range(n):
            s = 0
            for j in range(i, n):
                s += nums[j]
                max_return = max(s, max_return)
        return max_return
