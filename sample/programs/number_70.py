class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in self.cache:
            return self.cache[n]
        self.cache[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.cache[n]