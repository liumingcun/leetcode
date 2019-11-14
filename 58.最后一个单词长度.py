class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        num = 0
        for i in range(len(s)):
            if s[len(s)-1-i] == ' ':
                break
            num += 1
        return num