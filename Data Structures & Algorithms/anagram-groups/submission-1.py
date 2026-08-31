class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sol = []
        groups = {}

        for word in strs:
            sorted_list = sorted(word)
            sorted_word = ""
            for l in sorted_list:
                sorted_word +=l
            if sorted_word in groups:
                groups[sorted_word].append(word)
            else:
                groups[sorted_word]= [word] 
        
        for key in groups:
            sol.append(groups[key])
        return sol
        