from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        m, n = len(heights), len(heights[0])
        d = [(0,1),(1,0),(-1,0),(0,-1)]

        def bfs(starts):
            q = deque(starts)
            reach = set(starts)
            while q:
                r, c = q.popleft()
                for dr, dc in d:
                    nr, nc = r+dr, c+dc
                    if 0<=nr<m and 0<=nc<n and (nr,nc) not in reach \
                       and heights[nr][nc] >= heights[r][c]:
                        reach.add((nr,nc))
                        q.append((nr,nc))
            return reach

        pac_starts = []
        for r in range(m):
            pac_starts.append((r, 0))
        for c in range(n):
            pac_starts.append((0, c))

        atl_starts = []
        for r in range(m):
            atl_starts.append((r, n-1))
        for c in range(n):
            atl_starts.append((m-1, c))

        pac = bfs(pac_starts)
        atl = bfs(atl_starts)

        sol = []
        for r in range(m):
            for c in range(n):
                if (r, c) in pac and (r, c) in atl:
                    sol.append([r, c])
        return sol