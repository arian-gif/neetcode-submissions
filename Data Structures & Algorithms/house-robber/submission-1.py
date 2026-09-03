class Solution:
    def rob(self, nums: List[int]) -> int:
        size = len(nums)
        memo = {}

        def robber(i):
            if i<0 or i>=size:
                return 0
            if i in memo:
                return memo[i]
            memo[i] = max(nums[i]+robber(i+2),robber(i+1))
            return memo[i]
        return robber(0)
            
        
        
        