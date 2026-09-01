class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sol = []

        sorted_interval = sorted(intervals)
        print(sorted_interval)

        for start,end in sorted_interval:
            if sol and sol[-1][0]<=start<=sol[-1][1]:
                sol[-1][1] = max(sol[-1][1],end)
            else:
                sol.append([start,end])
        return sol