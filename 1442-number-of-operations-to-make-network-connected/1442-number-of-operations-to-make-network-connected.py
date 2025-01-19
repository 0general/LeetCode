class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if (len(connections) < n - 1) : return -1
        parent = [i for i in range(n)]
        def find(x):
            if parent[x] != x:
                return find(parent[x])
            return x
        def union(x, y):
            px = find(x)
            py = find(y)
            if px <= py:
                parent[py] = px
            else:
                parent[px] = py
        for x, y in connections:
            union(x, y)
        left = set()
        for i, x in enumerate(parent):
            parent[i] = find(x)
            left.add(parent[i])
        if len(left) <= 1:
            return 0
        else:
            return len(left) - 1