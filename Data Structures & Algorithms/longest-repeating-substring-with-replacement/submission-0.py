class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l,max_freq,best = -1,0,0

        for r,c in enumerate(s):
            count[c]=count.get(c,0)+1
            max_freq = max(max_freq,count[c])
            if (r-l) - max_freq>k:
                l+=1
                count[s[l]]-=1
            best = max(best, r-l)
        return best

        