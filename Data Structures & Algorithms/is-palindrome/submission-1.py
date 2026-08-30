class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not self.alphaNum(s[left]):
                left += 1
            while right > left and not self.alphaNum(s[right]):
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

    # Testing that it is an alphanumeric characters,
    # that's what the palindrome is testing
    # removes punctuation and spaces
    def alphaNum(self, element):
        return (ord('A') <= ord(element) <= ord('Z') or
                ord('a') <= ord(element) <= ord('z') or
                ord('0') <= ord(element) <= ord('9'))

  