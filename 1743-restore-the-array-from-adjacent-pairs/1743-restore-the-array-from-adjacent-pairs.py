from collections import defaultdict
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        dic = defaultdict(list)
        visited = set()
        for a, b in adjacentPairs:
            dic[a].append(b)
            dic[b].append(a)
        result = []
        for key, value in dic.items():
            if len(value) == 1:
                result.extend([key, value[0]])
                visited.update(result)
                break
        key = result[-1]
        while True:
            for i in dic[key]:
                if i not in visited:
                    visited.add(i)
                    result.append(i)
                    break
            if key == result[-1]:
                break
            key = result[-1]
        
        return result    
        