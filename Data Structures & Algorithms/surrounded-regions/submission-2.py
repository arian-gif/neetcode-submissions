from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return
        rows, cols = len(board), len(board[0])
        q = deque()

        # 1. seed the queue with every border O
        for r in range(rows):
            for c in range(cols):
                if (r == 0 or r == rows-1 or c == 0 or c == cols-1) and board[r][c] == "O":
                    q.append((r, c))
                    board[r][c] = "S"      # mark safe on enqueue

        # 2. BFS flood through connected O's, marking them safe
        while q:
            r, c = q.popleft()
            for nr, nc in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "O":
                    board[nr][nc] = "S"    # mark on enqueue, not dequeue
                    q.append((nr, nc))

        # 3. sweep: unreached O -> captured, S -> restored
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "S":
                    board[r][c] = "O"