class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        seen = set()
        l,best,curr = -1,0,0

        for r in range(len(s)):
            while s[r] in seen:
                l+=1
                seen.remove(s[l])
            seen.add(s[r])
            curr = r-l
            best = max(curr,best)
        return best 

        