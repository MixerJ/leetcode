class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # another solution
        # s_array = s.strip().split(' ')
        # return len(s_array[-1])
        s_array = s.split(' ')
        last_s = ''
        for string in s_array:
            if len(string) != 0:
                last_s = string
        return len(last_s)
