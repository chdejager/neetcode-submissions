class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numbers.sort()

        left = 0
        right = len(numbers) - 1

        result = []

        while left < right:
            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                result.append(numbers[left])
                result.append(numbers[right])
                return result
        

        return []