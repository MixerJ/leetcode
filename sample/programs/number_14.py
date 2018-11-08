class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        first_strs = [strs[0]] * len(strs)

        for i in range(1, len(strs)):
            while not strs[i].startswith(first_strs[i-1]):
                first_strs[i-1] = first_strs[i-1][:-1]
            first_strs[i] = first_strs[i-1]
        return first_strs[-1]
