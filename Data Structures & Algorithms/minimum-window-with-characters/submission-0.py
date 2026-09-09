class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        right = 0

        if t == "":
            return ""

        need = {}
        for char in t:
            need[char] = need.get(char, 0) + 1

        window = {}
        have = 0
        need_count = len(need)
        result = [-1, -1]
        result_len = float("inf")

        for right in range(len(s)):
            char = s[right]

            window[char] = window.get(char, 0) + 1

            if char in need and window[char] == need[char]:
                have += 1
            
            while have == need_count:
                if right - left +1 < result_len:
                    result = [left, right]
                    result_len = right - left + 1
                
                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1
                
                left += 1
        l, r = result

        if result_len == float("inf"):
            return ""
        
        return s[l:r + 1]

