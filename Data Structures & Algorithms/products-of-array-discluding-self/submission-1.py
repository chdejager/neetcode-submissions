class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1. Find the product of all and divide for each position
        # 2. (without division) find the product of everything to its 
        # left and then find the product of everything to its right

        res = [1] * len(nums)
        prefix = 1
        suffix = 1

        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        
        return res






