
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        record = [False]*n
        visited = [False]*n
        
        def dfs(node):
            if visited[node]:
                return record[node]
            visited[node] = True
            if len(graph[node]) == 0:
                record[node] = True
                return True

            ans = True
            for x in graph[node]:
                ans &= dfs(x)
            record[node] = ans
            return record[node]
        
        ans = []
        for i in range(n):
            if dfs(i):
                ans.append(i)
        return ans
        
        