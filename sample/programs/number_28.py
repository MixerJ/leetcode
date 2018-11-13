class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0 or not needle:
            return 0
        first = needle[0]
        for index in range(len(haystack)):
            single = haystack[index]
            if single == first:
                max_index = index+len(needle)
                if max_index > len(haystack):
                    return -1
                strs = haystack[index: max_index]
                if strs == needle:
                    return index
        return -1
