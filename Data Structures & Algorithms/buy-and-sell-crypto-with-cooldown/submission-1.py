class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        def dp(i, state):
            if i >= len(prices):
                return 0
            else:
                match state:
                    case 'buy':
                        # you either sell (calculate profit) 
                        # or stay in the buy state
                        return max(
                            dp(i+1, 'sell') - prices[i],
                            dp(i+1, 'buy')
                        )
                    case 'sell':
                        # you either cooldown or remain 
                        # in sell state(sell at a later date)
                        return max(
                            dp(i+1, 'cooldown') + prices[i],
                            dp(i+1, 'sell')
                        )
                    case _ :
                        return dp(i+1, 'buy')
        
        return dp(0, 'buy')
        







