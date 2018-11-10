class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        indexs = 0
        for num in nums:
            if indexs < 1 or num != nums[indexs - 1]:
                nums[indexs] = num
                indexs += 1
        # print (nums[:indexs])
        return indexs
