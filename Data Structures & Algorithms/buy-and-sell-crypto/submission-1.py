class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_price = float('inf')
        max_value = 0

        for p in prices:
            min_price = min(min_price,p)
            max_value = max(max_value,p-min_price)
        return max_value

        

        