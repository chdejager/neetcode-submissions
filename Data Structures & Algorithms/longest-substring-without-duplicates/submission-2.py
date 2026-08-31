class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0
        right = 0
        seen = set()

        result = 0
        
        while right < len(s):
            if s[right] not in seen:
                seen.add(s[right])
                result = max(result, right - left + 1)
                right += 1
            else:
                seen.remove(s[left])
                left += 1
        
        return result



    