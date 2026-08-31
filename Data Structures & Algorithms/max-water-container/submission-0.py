class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0,len(heights)-1
        m = 0

        while r>l:
            h=min(heights[r],heights[l])
            m = max((r-l)*h,m)

            if heights[l]>heights[r]:
                r-=1
            else:
                l+=1
            
        return m
