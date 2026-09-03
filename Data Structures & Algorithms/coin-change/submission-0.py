class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.memo = {}



        def dfs(amount):
            if amount == 0:
                return 0
            if amount < 0:
                return float('inf')
            if amount in self.memo:
                return self.memo[amount]
            best = float('inf')
            for coin in coins:
                best = min(best,1+dfs(amount-coin))
            
            self.memo[amount] = best
            return best
        return dfs(amount) if dfs(amount) != float('inf') else -1        

        
            
        




        