class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # _dict = {
        #    sorted_word: []
        # }
        _dict = {}
        
        for word in strs:
            sorted_word = sorted(word)
            source=""
            for l in sorted_word:
                source+=l
            if source not in _dict:
                _dict[source]=[]
            _dict[source].append(word)

        sol = []

        for key in _dict:
            sol.append(_dict[key])
        

        return sol
        