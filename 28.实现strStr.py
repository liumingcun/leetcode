class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if len(needle) > len(haystack):
            return -1

        i = 0
        while i < len(haystack):
            if haystack[i:i + len(needle)] == needle:
                return i
            else:
                if len(haystack) - i - 1 == len(needle) - 1:
                    return -1
                i += 1


###############暴力匹配################
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if len(needle) > len(haystack):
            return -1

        i = 0
        j = 0
        while i < len(haystack) and j < len(needle):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                i = i - j + 1
                j = 0

        if j == len(needle):
            return i - j
        else:
            return -1

