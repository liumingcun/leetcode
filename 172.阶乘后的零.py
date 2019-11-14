class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        temp1 = 0
        for i in range(100):
            if n < 5 ** (i + 1) and n >= 5 ** i:
                temp1 = 5 ** i
                break
        while temp1 >= 5:
            ans += int(n / temp1)
            temp1 /= 5
        return ans



