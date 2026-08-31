class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        left = 0
        count = {}
        result = 0

        for right in range(len(s)):
            
            if s[right] in count:
                count[s[right]] += 1
            else:
                count[s[right]] = 1
            
            max_freq = max(count.values())

            replacements = (right - left + 1) - max_freq

            if replacements <= k:
                result = max(result, right - left + 1)
                right += 1
            else:
                left += 1
        
        return result
            
