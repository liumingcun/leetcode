class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        list = [-1] * (N + 1)
        list[0] = 0
        list[1] = 1
        i = 2
        while i <= N:
            list[i] = list[i - 1] + list[i - 2]
            i += 1
        return list[N]