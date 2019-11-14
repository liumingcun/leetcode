class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_int = int(a, 2)
        b_int = int(b, 2)
        num = int(a_int) + int(b_int)
        result = str(bin(num))
        i = 2
        new_result = ''
        while i < len(result):
            new_result += result[i]
            i += 1
        return new_result

