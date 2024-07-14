class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        def parent_find(i, t):
            if i != parent[i][t]:
                parent[i][t] = parent_find(parent[i][t], t)
            return parent[i][t]
        
        def union(i, j, t):
            i, j = parent_find(i, t), parent_find(j, t)
            if i == j:
                return False
            parent[i][t] = j
            return True
        
        parent = [[i, i] for i in range(n + 1)]
        
        result = 0
        alice_edge = 0
        bob_edge = 0
        
        edges.sort(reverse=True)
        for t, u, v in edges:
            if t == 1:
                if union(u, v, 0):
                    alice_edge += 1
                else:
                    result += 1
            elif t == 2:
                if union(u, v, 1):
                    bob_edge += 1
                else:
                    result += 1
            else:
                if union(u, v, 0) and union(u, v, 1):
                    alice_edge += 1
                    bob_edge += 1
                else:
                    result += 1
        return result if (alice_edge == bob_edge == n - 1) else -1