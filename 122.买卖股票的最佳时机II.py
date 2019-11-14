class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        len_p = len(prices)
        for i in range(len_p - 1):
            if prices[i+1] > prices[i]:
                profit += prices[i+1] - prices[i]
            
        return profit