class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        sol = max(piles)

        while l<=r:
            m = (l+r)//2
            print(l,r,m)
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/m)
                
            if hours<=h:
                sol = m
                r = m-1
            else:
                l=m+1
        
        return sol

        