from collections import deque
from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        
        visited = [False] * n
        complete_count = 0
        
        for i in range(n):
            if visited[i]:
                continue
            
            q = deque([i])
            visited[i] = True
            comp_nodes = []
            
            while q:
                u = q.popleft()
                comp_nodes.append(u)
                for v in g[u]:
                    if not visited[v]:
                        visited[v] = True
                        q.append(v)
            
            k = len(comp_nodes)
            # undirected 그래프에서 요소 내부 간선 수 = (요소 내 각 정점 차수 합)/2
            deg_sum = sum(len(g[u]) for u in comp_nodes)
            e = deg_sum // 2
            
            # 완전 그래프라면 e == k*(k-1)//2
            if e == k * (k - 1) // 2:
                complete_count += 1
        
        return complete_count