class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        left = 0
        right = 1
        maxProfit = 0

        while right < n:
            if prices[right] > prices[left]:
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit, profit)
            else:
                left = right
            right += 1
        
        return maxProfit


