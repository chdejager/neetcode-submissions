class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        #Base Case'=
        if n <= 1:
            return s

        longest = ''

        for center in range(n):
            #if odd palindrome
            left = right = center
            while left >= 0 and right < n and s[left] == s[right]:
                substring = s[left:right + 1]
                if len(substring) > len(longest):
                    longest = substring
                left -= 1
                right += 1
            
            #if even palindrome
            left, right = center, center + 1
            while left >= 0 and right <n and s[left] == s[right]:
                substring = s[left:right + 1]
                if len(substring) > len(longest):
                    longest = substring
                left -= 1
                right += 1

        return longest
            
            
            
