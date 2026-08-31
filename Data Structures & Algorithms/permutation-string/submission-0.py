class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False

        in_s1 = {}

        for i in range(len(s1)):
            if s1[i] in in_s1:
                in_s1[s1[i]] += 1
            else:
                in_s1[s1[i]] = 1
        
        window = {}
        left = 0

        for right in range(len(s2)):
            if s2[right] in window:
                window[s2[right]] += 1
            else:
                window[s2[right]] = 1
            
            if sum(window.values()) > len(s1):
                window[s2[left]] -= 1

                if window[s2[left]] == 0:
                    del window[s2[left]]

                left += 1
            
            if window == in_s1:
                return True
            
        return False





