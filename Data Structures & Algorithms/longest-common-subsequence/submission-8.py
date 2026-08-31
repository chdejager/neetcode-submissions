class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        # Making the grid and filling it with 0s
        dp = []
        m = len(text1)
        n = len(text2)

        for _ in range(m + 1):
            dp.append([0] * (n + 1))
        
        # We do not need a base case
        # don't know if the first letters are matching or not

        for i in range(m + 1):
            for j in range(n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1 
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])


        return dp[m - 1][n - 1]
                    











