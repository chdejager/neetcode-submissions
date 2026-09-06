class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()

        if not nums:
            return 0

        current = 1
        longest = 1

        for i in range(len(nums) - 1):
            if nums[i] + 1 == nums[i+1]:
                current += 1
            elif nums[i] == nums[i+1]:
                continue
            else:
                current = 1

            longest = max(longest, current)
        
        return longest
