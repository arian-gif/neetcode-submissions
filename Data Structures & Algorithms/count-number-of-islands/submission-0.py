from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.count = 0
        self.col = len(grid[0])
        self.row = len(grid)
        
        def bfs(r,c):
            q = deque([[r,c]])

            while q:
                r,c=q.pop()
                print(r,c)
                grid[r][c]= "0"

                right = [r,c+1] if c+1<self.col else None
                left = [r,c-1] if c-1>=0 else None
                down = [r+1,c] if r+1<self.row else None
                up = [r-1,c] if r-1>=0 else None

                if right:
                    if grid[r][c+1]=="1":
                        q.append(right)
                if left:
                    if grid[r][c-1]=="1":
                        q.append(left)
                if up:
                    if grid[r-1][c]=="1":
                        q.append(up)
                if down:
                    if grid[r+1][c]=="1":
                        q.append(down)
                

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] =="1":
                    print(f"top level:{r},{c}")
                    bfs(r,c)
                    self.count +=1
        

        return self.count

        