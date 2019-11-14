class Solution:
    def longestCommonPrefix(self, strs):
        s = strs
        a = ""
        len_1 = 100
        a_short = 0
        if len(s) == 0:
            return ""
        for i in range(len(s)):
            if len(s[i]) < len_1:
                len_1 = len(s[i])
                a_short = i
        # print(len_1, a_short)
        for i in range(len_1):
            num = 0
            a1 = s[a_short][i]
            for j in range(len(s)):
                # print(a1)
                if s[j][i] == a1:
                    num += 1
            if num == len(s):
                a += s[a_short][i]
            else:
                break
        if a == "":
            return ""
        else:
            return a