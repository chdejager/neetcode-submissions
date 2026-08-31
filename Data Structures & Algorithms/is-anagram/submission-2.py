class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = set()

        if len(s) != len(t):
            return False

        for i in s:
            if s[i] not in seen:
                seen.add(s[i])
        
        for j in t:
            if t[i] not in seen:
                return False

        return True