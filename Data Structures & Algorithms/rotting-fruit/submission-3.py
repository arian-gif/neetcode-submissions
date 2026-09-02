from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        m,n = len(grid), len(grid[0])
        fresh = set()
        q = deque()

        for r in range(m):
            for c in range(n):
                if grid[r][c]==2:
                    q.append((r,c))
                elif grid[r][c]==1:
                    fresh.add((r,c))
        time = 0
        d = [(1,0),(0,1),(-1,0),(0,-1)]
        while q and fresh:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr,dc in d:
                    nr,nc = r+dr, c+dc
                    if 0<=nr<m and 0<=nc<n and grid[nr][nc]==1:
                        grid[nr][nc]="2"
                        fresh.remove((nr,nc))
                        q.append((nr,nc))
            time+=1
        if fresh:
            return -1
        else:
            return time




            


        