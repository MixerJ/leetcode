class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict = {}
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return [lookup[target-num], i]
            else:
                lookup[num] = i
