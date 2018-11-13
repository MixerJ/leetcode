class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return_index = 0
        if target < nums[0]:
            return 0
        for index in range(len(nums)):
            num = nums[index]
            if num == target:
                return_index = index
                break
            if num < target:
                return_index = index + 1
        return return_index
