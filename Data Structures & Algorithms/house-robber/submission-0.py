class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float('inf')] * (n + 1)

        #Base Case
        dp[0] = 0
        dp[1] = nums[0]
        # dp[3] = max(nums[0], nums[1])
        
        for i in range(2, n + 1):
            option1 = dp[i - 1]
            option2 = dp[i - 2] + nums[i - 1]
            dp[i] = max(option1, option2)
        return dp[n]