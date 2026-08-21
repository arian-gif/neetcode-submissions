class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sol = []
        freq = {}

        for n in nums:
            if n in freq:
                freq[n] = freq[n]+ 1
            else:
                freq[n]=1
                
        heap = []
        for key in freq:
            heapq.heappush(heap,(freq[key],key))
            if len(heap)>k:
                heapq.heappop(heap)
        for i in range(k):
            sol.append(heapq.heappop(heap)[1])
        

        return sol
        