from collections import deque
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        num = 0
        visited = [False]*n
        indegree = [[] for _ in range(n)] # no need to change edge 
        outdegree = [[] for _ in range(n)] # target edge
        for f,t in connections:
            outdegree[f].append(t)
            indegree[t].append(f)
        visited[0] = True
        q = deque()
        q.append(0)
        while q:
            now = q.popleft()
            for i in indegree[now]:
                if not visited[i]:
                    visited[i] = True
                    q.append(i)
            for j in outdegree[now]:
                if not visited[j]:
                    visited[j] = True
                    num += 1
                    q.append(j)
        return num
            
        
        