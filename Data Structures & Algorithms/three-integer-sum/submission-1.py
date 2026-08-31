class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        result = []

        # must iterate i throughout nums
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            j = i + 1
            k = len(nums) - 1
            target = -nums[i]
            
            while j < k:
                current = nums[j] + nums[k]

                if target < current:
                    k -= 1
                elif target > current:
                    j += 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
        return result

