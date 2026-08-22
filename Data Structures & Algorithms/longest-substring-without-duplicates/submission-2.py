class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ind = {}
        l, best = 0, 0

        for r in range(len(s)):
            if s[r] in ind and ind[s[r]] >= l:
                l = ind[s[r]] + 1
            ind[s[r]] = r
            best = max(best, r - l + 1)
        return best