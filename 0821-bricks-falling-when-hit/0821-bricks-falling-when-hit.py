class DSU:
    def __init__(self, n):
        self.p = list(range(n))
        self.sz = [1] * n
    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x
    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return
        if self.sz[ra] < self.sz[rb]:
            ra, rb = rb, ra
        self.p[rb] = ra
        self.sz[ra] += self.sz[rb]
    def size(self, x):
        return self.sz[self.find(x)]

class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        R, C = len(grid), len(grid[0])
        top = R * C
        def idx(r, c): return r * C + c
        g = [row[:] for row in grid]
        for r, c in hits:
            if g[r][c] == 1:
                g[r][c] = 0
            else:
                g[r][c] = -1
        dsu = DSU(R * C + 1)
        def try_union(r, c):
            if r == 0:
                dsu.union(idx(r, c), top)
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and g[nr][nc] == 1:
                    dsu.union(idx(r, c), idx(nr, nc))
        for r in range(R):
            for c in range(C):
                if g[r][c] == 1:
                    try_union(r, c)
        ans = []
        for r, c in reversed(hits):
            if grid[r][c] == 0:
                ans.append(0)
                continue
            prev = dsu.size(top)
            g[r][c] = 1
            try_union(r, c)
            curr = dsu.size(top)
            added = max(0, curr - prev - 1)
            ans.append(added)
        return ans[::-1]