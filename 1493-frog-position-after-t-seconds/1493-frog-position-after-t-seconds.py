
class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        if n == 1: return 1.0
        e = [[] for _ in range(n + 1)]
        for p, c in edges:
            e[p].append(c)
            e[c].append(p)
        visited = [0] * (n + 1)
        
        def dfs(i, t):
            if i != 1 and len(e[i]) == 1 or t == 0:
                return i == target
            visited[i] = 1
            res = sum(dfs(j, t - 1) for j in e[i] if not visited[j])
            return res * 1.0 / (len(e[i]) - (i != 1))
        return dfs(1, t)