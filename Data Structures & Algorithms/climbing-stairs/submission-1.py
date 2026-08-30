class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)

        #Base Case
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            option1 = dp[i - 1]
            option2 = dp[i - 2]
            dp[i] = option1 + option2

        return dp[n]