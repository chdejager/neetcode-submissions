class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for word in strs:
            result += str(len(word))
            result += "#"
            result += word

        return result   

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        j = 0

        while i < len(s):
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            word = s[j + 1: length + j + 1]

            result.append(word)

            i = length + j + 1
            j = i
        
        return result


