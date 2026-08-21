from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.max_rows=len(grid)
        self.max_cols=len(grid[0])
        self.good_orange = set()


        def rot(rotten_orange):
            q = deque(rotten_orange)
            minutes = 0

            while q and self.good_orange:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    for nr, nc in [(r,c+1),(r,c-1),(r+1,c),(r-1,c)]:
                        if 0<=nr<self.max_rows and 0<=nc<self.max_cols and grid[nr][nc]==1:
                            q.append([nr,nc])
                            grid[nr][nc]=2
                            self.good_orange.remove((nr,nc))
                minutes+=1
            return minutes

        rotten_list=[]

        for r in range(self.max_rows):
            for c in range(self.max_cols):
                if grid[r][c]==2:
                    rotten_list.append([r,c])
                if grid[r][c]==1:
                    self.good_orange.add((r,c))
        minutes = rot(rotten_list)

        return minutes if len(self.good_orange)==0 else -1

        