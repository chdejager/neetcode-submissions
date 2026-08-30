class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        #Base Case
        if n <= 1:
            return s

        longest = ''

        # Helper function
        def check_palindrome(left, right):
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        for center in range(n):
            #if odd palindrome
            left = right = center
            longest1 = check_palindrome(left, right)

            #if even palindrome
            left, right = center, center + 1
            longest2 = check_palindrome(left, right)

            longer = longest1 if len(longest1) > len(longest2) else longest2
            
            if len(longer) > len(longest):
                longest = longer

        return longest
            
            
            
