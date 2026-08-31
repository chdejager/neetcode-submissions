class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 1
        seen = set()
        max_len = 1

        while r < len(s):
            seen.add(s[l])
            if s[r] not in seen:
                seen.add(s[r])
                max_len = max(max_len, r - l + 1)
            else: 
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
                seen.add(s[r])
            r += 1
        
        return max_len
