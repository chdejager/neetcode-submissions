class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = set()

        if len(s) != len(t):
            return False

        for i in s:
            if i not in seen:
                seen.add(i)
        
        for j in t:
            if j not in seen:
                return False

        return True