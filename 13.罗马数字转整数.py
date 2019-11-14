class Solution:
    def romanToInt(self, s: str) -> int:
        len_str = len(s)
        num = 0
        i = 0
        while i < len_str:
            if s[i] == 'V':
                num += 5
                i += 1
                continue
            if s[i] == 'L':
                num += 50
                i += 1
                continue
            if s[i] == 'D':
                num += 500
                i += 1
                continue
            if s[i] == 'M':
                num += 1000
                i += 1
                continue
            if s[i] == 'I':
                if i != len(s) - 1:
                    if s[i + 1] == 'V':
                        num += 4
                        i += 2
                        continue
                    if s[i + 1] == 'X':
                        num += 9
                        i += 2
                        continue
                num += 1
                i += 1
                continue
            if s[i] == 'X':
                if i != len(s) - 1:
                    if s[i + 1] == 'L':
                        num += 40
                        i += 2
                        continue
                    if s[i + 1] == 'C':
                        num += 90
                        i += 2
                        continue
                num += 10
                i += 1
                continue
            if s[i] == 'C':
                if i != len(s) - 1:
                    if s[i + 1] == 'D':
                        num += 400
                        i += 2
                        continue
                    if s[i + 1] == 'M':
                        num += 900
                        i += 2
                        continue
                num += 100
                i += 1
                continue
        return num


class Solution_2:
    def romanToInt(self, s: str) -> int:
        num = 0
        dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        for i in range(len(s)):
            if i < len(s)-1 and dic[s[i]]<dic[s[i+1]]:
                num -= dic[s[i]]
            else:
                num += dic[s[i]]
        return num