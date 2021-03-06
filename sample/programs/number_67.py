class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if a == '' or b == '':
            return a + b
        if a[-1] == '0' and b[-1] == '0':
            return self.addBinary(a[:-1], b[:-1]) + '0'
        elif a[-1] == '1' and b[-1] == '1':
            return self.addBinary(a[:-1], self.addBinary(b[:-1], '1')) + '0'
        else:
            return self.addBinary(a[:-1], b[:-1]) + '1'
