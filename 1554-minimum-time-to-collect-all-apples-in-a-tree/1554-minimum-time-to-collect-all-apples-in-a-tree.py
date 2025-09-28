from collections import defaultdict
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        g = defaultdict(list)
        for a,b in edges:
            g[a].append(b); g[b].append(a)
        def dfs(u, p):
            total = 0
            for v in g[u]:
                if v == p: 
                    continue
                t = dfs(v, u)
                if t > 0 or hasApple[v]:
                    total += t + 2
            return total
        return dfs(0, -1)