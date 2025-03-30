class Solution:
    def dfs(self, x, curr, ans, children):
        for c in children[curr]:
            if not ans[c] or ans[c][-1] != x:
                ans[c].append(x)
                self.dfs(x, c, ans, children)

    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ans = [[] for _ in range(n)]
        children = [[] for _ in range(n)]
        for i, j in edges:
            children[i].append(j)
        for i in range(n):
            self.dfs(i,i,ans,children)
        return ans