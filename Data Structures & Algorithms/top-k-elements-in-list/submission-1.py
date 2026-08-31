class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for n in nums:
            if n in freq:
                freq[n]+=1
            else:
                freq[n]=1

        order = []

        for key in freq:
            order.append((freq[key],key))  
        order = sorted(order,reverse=True)
        
        sol = []
        
        for i in range(k):
            sol.append(order[i][1])

        return sol