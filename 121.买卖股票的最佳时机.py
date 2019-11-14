class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        len_p = len(prices)
        if len_p == 1 or len_p == 0:
            return 0
        profit = 0
        temp = prices[0]
        i = 1
        while i < len_p:
            if prices[i] < temp:
                temp = prices[i]
            elif prices[i] - temp > profit:
                profit = prices[i] - temp
            i += 1
        return profit

