import math

# 참고 : https://leetcode.com/problems/count-valid-paths-in-a-tree/discuss/4084168/PythonC%2B%2B-dfs-solution-with-explanation

mx = 10 ** 5 + 1
# 소수 구하기
prime = [True] * mx
prime[1] = False
        
for i in range(2, math.isqrt(mx) + 1):
    if prime[i]:
        for j in range(i * i, mx, i):
            prime[j] = False

class Solution:
    def countPaths(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n + 1)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        
        node = []
        def dfs(curr, prev):
            node.append(curr)
            for i in g[curr]:
                if not prime[i] and i != prev:
                    dfs(i, curr)
        
        size = [0] * (n+1)
        ans = 0
        for i in range(1, n + 1):
            if not prime[i]:
                continue
            s = 0
            for j in g[i]:
                if prime[j]:
                    continue
                if size[j] == 0:
                    node.clear()
                    dfs(j, -1)
                    for x in node:
                        size[x] = len(node)
                ans += size[j] * s
                s += size[j]
            ans += s
        return ans