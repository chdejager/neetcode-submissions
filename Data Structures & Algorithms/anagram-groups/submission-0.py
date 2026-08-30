class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = {}

        for word in strs:
            word_list = list(word)
            word_list.sort()
            sorted_word = "".join(word_list)
            
            if sorted_word in groups:
                groups[sorted_word].append(word)
            else:
                groups[sorted_word] = [word]
        
        final_list = list(groups.values())
        return final_list



