class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #step 1> sort the intervals, guarantees the start is ordered
        intervals.sort(key=lambda x:x[0])
        merged =[]
        for s, e in intervals:
            if merged and s<=merged[-1][1]:
                merged[-1][1]= max(merged[-1][1],e)
            else:
                merged.append([s,e])
        return merged