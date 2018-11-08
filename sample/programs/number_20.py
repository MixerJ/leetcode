class Solution:
    parentheses = {
        '(': ')',
        '[': ']',
        '{': '}'
    }

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if len(s) % 2 == 1:
            return False
        s = [i for i in s]
        index = 0
        while len(s) > 0:
            if index >= len(s) - 1:
                return False
            pre = s[index]
            last = s[index+1]

            if pre not in self.parentheses.keys():
                return False
            elif last in self.parentheses.keys():
                index += 1
            elif self.parentheses[pre] == last:
                s.pop(index+1)
                s.pop(index)
                index = 0 if index - 1 < 0 else index - 1
            else:
                return False
        return s == []

    def stackCheckIsValid(self, s):
        leftP = '([{'
        rightP = ')]}'
        stack = []

        for char in s:
            if char in leftP:
                stack.append(char)

            if char in rightP:
                if not stack:
                    return False
                temp = stack.pop()
                if self.parentheses[temp] == char:
                    continue
                # if char == ')' and temp == '(':
                #     continue
                # elif char == ']' and temp == '[':
                #     continue
                # elif char == '}' and temp == '{':
                #     continue
                else:
                    return False

        return stack == []
