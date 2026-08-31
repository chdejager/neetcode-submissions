class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}

        if len(s) != len(t):
            return False

        for i in s:
            if i in count:
                count[i] =+ 1
            else:
                count[i] = 1
        
        for j in t:
            if j in count:
                if count[j] == 0:
                    return False
                else:
                    count[j] =- 1
            return False

        return True



