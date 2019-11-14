class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        numRows = rowIndex+1
        ans = []
        a = [1]
        ans.append(a)
        if numRows == 0:
            return []
        elif numRows == 1:
            return ans[0]
        i = 2
        x = [1]
        while i < numRows + 1:
            temp = [0] * i
            for j in range(len(temp)):
                if j == 0:
                    temp[j] = x[j]
                elif j == len(temp)-1:
                    temp[j] = x[-1]
                else:
                    temp[j] = x[j-1] + x[j]
            i += 1
            ans.append(temp)
            x = temp
        return ans[rowIndex]