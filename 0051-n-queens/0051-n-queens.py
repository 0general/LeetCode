class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        cols = set()
        diag = set()
        anti = set()
        board = [["."] * n for _ in range(n)]

        def backtrack(r: int):
            if r == n:
                res.append(["".join(row) for row in board])
                return
            for c in range(n):
                if c in cols or (r - c) in diag or (r + c) in anti:
                    continue
                board[r][c] = "Q"
                cols.add(c); diag.add(r - c); anti.add(r + c)

                backtrack(r + 1)

                board[r][c] = "."
                cols.remove(c); diag.remove(r - c); anti.remove(r + c)

        backtrack(0)
        return res