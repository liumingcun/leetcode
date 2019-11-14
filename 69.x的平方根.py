class Solution:
    def mySqrt(self, x: int) -> int:
        a, b = self.jiou(0, x, x)
        i = 0
        while i < 1:
            if pow(a, 2) == x:
                return int(a)
            elif pow(a, 2) < x and pow(a + 1, 2) > x:
                return int(a)
            else:
                a, b = self.jiou(a, b, x)

    def jiou(self, num_1, num_2, x):
        if pow(num_1, 2) < x and pow(num_2, 2) > x:

            if (num_1 + num_2) % 2 == 0:
                b = (num_1 + num_2) / 2
            else:
                b = (num_1 + num_2 + 1) / 2
            if pow(b, 2) < x:
                return b, num_2
            else:
                return num_1, b

        else:
            return num_2, num_2


class Solution:
    def mySqrt(self, x: int) -> int:
        a = x ** 0.5
        return int(a)


# 牛顿迭代法
class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        r = x
        while r > x / r:
            r = (r + x / r) // 2
        return int(r)


# http://www.matrix67.com/blog/archives/361
# https://blog.csdn.net/ccnt_2012/article/details/81837154
