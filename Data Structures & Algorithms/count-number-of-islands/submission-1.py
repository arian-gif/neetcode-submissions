from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        m,n = len(grid),len(grid[0])
        self.q = deque()

        def bfs(r,c):
            self.q.append([r,c])
            d = [(1,0),(0,1),(-1,0),(0,-1)]
            while self.q:
                r,c = self.q.popleft()
                for dr,dc in d:
                    if 0<=r+dr<m and 0<=c+dc<n and grid[r+dr][c+dc]=="1":
                        self.q.append([r+dr,c+dc])
                        grid[r+dr][c+dc]="0"


        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c]=="1":
                    count+=1
                    grid[r][c]="0"
                    bfs(r,c)
        return count

        

        