class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start = set()
        end = set()
        for path in paths:
            s, e = path
            if s in end:
                end.remove(s)
            else:
                start.add(s)
            if e in start:
                start.remove(e)
            else:
                end.add(e)
        return end.pop()