class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        s,f = 0,0
        max_val = 0

        while f<len(prices):
            diff = prices[f]-prices[s]
            if diff<0:
                s+=1
            else:
                f+=1
            max_val = max(max_val,diff)
        
        return max_val

        

        