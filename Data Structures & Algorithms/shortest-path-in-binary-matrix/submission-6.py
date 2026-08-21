from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        max_rows = len(grid)
        max_cols = len(grid[0])
        start = grid[0][0]
        end = grid[max_rows-1][max_cols-1]
        if start ==1 or end==1:
            return -1

        q=deque([[0,0,1]])
        grid[0][0]=1

        while q:
            for _ in range(len(q)):
                r,c,d = q.popleft()
                if (r,c)==(max_rows-1,max_cols-1):
                        return d
                for dr, dc in [(0,1),(1,0),(-1,0),(0,-1),(-1,-1),(1,1),(1,-1),(-1,1)]:
                    nr,nc = r+dr, c+dc
                    if 0<=nr<max_rows and 0<=nc<max_cols and grid[nr][nc]==0:
                        grid[nr][nc]=1
                        q.append([nr,nc,d+1])
        return -1





        


        