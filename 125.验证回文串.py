class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        list1 = []
        for i in range(len(s)):
            if s[i].isalpha() or s[i].isdigit():
                list1.append(s[i])
        a = list(reversed(list1))
        print(a)
        if list1 ==  a:
            return True
        else:
            return False


class Solution:
    def isPalindrome(self, s: str) -> bool:

        list1 = []
        list2 = []
        for i in range(len(s)):
            if ord(s[i]) >= 48 and ord(s[i]) <= 57:
                list1.append(s[i])
            elif s[i] >= 'a' and s[i] <= 'z':
                list1.append(s[i])
            elif s[i] >= 'A' and s[i] <= 'Z':
                list1.append(chr(ord(s[i]) + 32))

        len_list1 = len(list1)

        for i in range(len_list1):
            if list1[i] != list1[len_list1 - 1 - i]:
                return False
        return True
