class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float('inf')] * (n + 1)

        #Base Case
        dp[0] = 0
        dp[1] = nums[0]
        
        
        for i in range(2, n + 1):
            #skip
            option1 = dp[i - 1]
            #rob
            option2 = dp[i - 2] + nums[i - 1]
            dp[i] = max(option1, option2)
        
        return dp[n]