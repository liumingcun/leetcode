
class Solution:
    def climbStairs(self, n: int) -> int:
        # if n == 1 or n == 0:
        #     return 1
        # return self.climbStairs(n-1) + self.climbStairs(n-2)
        list = [-1] * (n + 1)
        list[0] = 1
        list[1] = 1
        i = 2
        while i <= n:
            list[i] = list[i - 1] + list[i - 2]
            i += 1
        return list[n]
