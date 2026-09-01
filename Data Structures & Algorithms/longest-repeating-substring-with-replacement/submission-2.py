class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        l=0
        sol = 0

        for r in range(len(s)):
            if s[r] in freq:
                freq[s[r]]+=1
            else:
                freq[s[r]]=1
            most_freq = max(freq.values())
            if (r-l+1)-most_freq>k:
                if freq[s[l]] ==0:
                    freq[s[l]].pop()
                else:
                    freq[s[l]]-=1
                l+=1
            sol = max(sol,r-l+1)
        return sol




        