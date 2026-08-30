class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        #Storing solution
        counter = 0

        #Base Case, each letter is a palindrome so answer is at least len(n)
        # counter = n

        for center in range(n):
            left = right = center
            while left >= 0 and right < n and s[left] == s[right]:
                counter += 1
                left -= 1
                right += 1
            
            left, right = center, center + 1
            while left >= 0 and right < n and s[left] == s[right]:
                counter += 1
                left -= 1
                right += 1
        
        return counter

        
            


        