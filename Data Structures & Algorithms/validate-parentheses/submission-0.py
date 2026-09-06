class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        matches = {
            ")" : "(",
            "]" : "[",
            "}" : "{",
        }

        for char in s:
            if char not in matches:
                stack.append(char)
            else:
                if not stack:
                    return False
            
                if stack.pop() != matches[char]:
                    return False
            
        return len(stack) == 0