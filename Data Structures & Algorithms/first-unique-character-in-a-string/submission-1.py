class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = {}
        for let in s:
            seen[let] = seen.get(let,0)+1
        for i,let in enumerate(s):
            if seen[let]==1:
                return i
        return -1


        