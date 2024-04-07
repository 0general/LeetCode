class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parent = [i for i in range(n)]
        
        def find_parent(x):
            if parent[x] != x:
                parent[x] = find_parent(parent[x])
            return parent[x]
        def union_find(x, y):
            x, y = find_parent(x), find_parent(y)
            if x <= y:
                parent[y] = x
            else:
                parent[x] = y
        
        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j] == 1:
                    union_find(i, j)
        s = set()
        for i in range(n):
            s.add(find_parent(i))
        return len(s)