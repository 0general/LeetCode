class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = {chr(x): chr(x) for x in range(97, 123)}
        
        def union(s, c):
            ps, pc = find_parent(s), find_parent(c)
            if ord(ps) <= ord(pc):
                parent[pc] = ps
            else:
                parent[ps] = pc
            
        def find_parent(s):
            if s == parent[s]:
                return s
            parent[s] = find_parent(parent[s])
            return parent[s]
        
        for i in range(len(s1)):
            union(s1[i], s2[i])
        
        return "".join([find_parent(x) for x in baseStr])
                
                
        