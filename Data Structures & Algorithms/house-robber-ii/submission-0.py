class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        def helper(arr):
            m = len(arr)
            dp = [float('inf')] * (m + 1)

            dp[0] = 0
            dp[1] = arr[0]

            for i in range(2, m + 1):
                skip = dp[i - 1]
                rob = dp[i - 2] + arr[i - 1]
                dp[i] = max(skip, rob)
            
            return dp[m]

        option1 = helper(nums[1:])
        option2 = helper(nums[:n - 1])
        max_amount = max(option1, option2)


        return max_amount
