class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roma_number = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        result = 0
        for index in range(len(s)):
            if index > 0 and roma_number[s[index]] > roma_number[s[index-1]]:
                result += roma_number[s[index]] - 2 * roma_number[s[index-1]]
            else:
                result += roma_number[s[index]]
        return result
