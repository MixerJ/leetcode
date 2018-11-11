class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        indexs = 0
        for num in nums:
            if num != val:
                nums[indexs] = num
                indexs += 1

        # print (nums[:indexs])
        return indexs
