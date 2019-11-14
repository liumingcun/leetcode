class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x = str(x)
        new_x = x[::-1]
        # new_x = ''
        # for i in range(len(x)):
        #     new_x+=(x[len(x)-i-1])
        if new_x == x:
            return True