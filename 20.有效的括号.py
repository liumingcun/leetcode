class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        new_s = []
        list = ['{', '}', '[', ']', '(', ')']
        for i in range(len(s)):
            if s[i] in list:
                new_s.append(s[i])
                str = self.check(new_s)
        if len(new_s) == 0:
            return True
        else:
            return False

    def check(self, str):
        if len(str) >= 2:
            if str[-2] == '{' and str[-1] == '}':
                str.pop()
                str.pop()
                return str
            if str[-2] == '[' and str[-1] == ']':
                str.pop()
                str.pop()
                return str
            if str[-2] == '(' and str[-1] == ')':
                str.pop()
                str.pop()
                return str



