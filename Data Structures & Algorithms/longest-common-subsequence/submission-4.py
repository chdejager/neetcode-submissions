class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        # Making the grid and filling it with 0s
        dp = []
        m = len(text1)
        n = len(text2)

        for _ in range(m):
            dp.append([0] * n)
        
        # Base Case
        dp[0][0] = 0

        for i in range(m):
            for j in range(n):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1 
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])


        return dp[m - 1][n - 1]
                    











