class Solution:
    def simplifyPath(self, path: str) -> str:
        ans = []
        for p in path.split('/'):
            if p != '' and p != '.' and p != '..':
                ans.append(p)
            elif p == '..' and len(ans) > 0:
                ans.pop()
        return '/'+'/'.join(ans)
        