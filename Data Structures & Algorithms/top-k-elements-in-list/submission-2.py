class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Make a dictionary to count items
        # Order them in terms of frequency
        # pop the top 2

        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        ordered = sorted(freq, key = freq.get, reverse = True)

        return ordered[:k]
