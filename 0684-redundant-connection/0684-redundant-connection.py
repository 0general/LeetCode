class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        def parent_find(x):
            if x != parent[x]:
                parent[x] = parent_find(parent[x])
            return parent[x]
        
        def union(u, v):
            u, v = parent_find(u), parent_find(v)
            if u == v: return False
            if u < v:
                parent[v] = u
            else:
                parent[u] = v
            return True
        
        for u, v in edges:
            if not union(u, v):
                return [u, v]
        