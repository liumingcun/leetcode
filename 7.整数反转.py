class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        if len(x) > 32:
            return 0
        if x[0] == '-':
            x = x[::-1]
            x = x[0:-1]
            if x[0] == '0':
                x = x[1:len(x)]
            if int(x) > 2147483648:
                return 0
            return -int(x)
        if len(x) == 1 and x[0] == '0':
            x = int(x)
            return x
        x = x[::-1]
        if x[0] == '0' and len(x) != 1:
            x = x[1:len(x)]
        if int(x) > 2147483648:
            return 0
        return int(x)

