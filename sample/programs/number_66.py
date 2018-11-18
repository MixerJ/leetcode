class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # if len(digits) == 0:
        #     return [1]
        # if digits[-1] < 9:
        #     return digits[:-1] + [digits[-1] + 1]
        # else:
        #     return self.plusOne(digits[:-1]) + [0]
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            digits[i] += carry
            if digits[i] < 10:
                carry = 0
                break
            else:
                digits[i] = 0
        if carry == 1:
            digits.insert(0, 1)
        return digits
