class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        c = set()
        max_len =1
        l,r=0,1
        c.add(s[l])
        while r<len(s):
            if s[r] in c:
                c.remove(s[l])
                l+=1
            else:
                c.add(s[r])
                r+=1
                max_len= max(max_len,len(c))
            
        return max_len
        