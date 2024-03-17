class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        items1.extend(items2)
        items1.sort(key=lambda x: x[0])
        ret = []
        for idx, item in enumerate(items1):
            if idx != 0 and item[0] == ret[-1][0]:
                ret[-1][1] += item[1]
                continue
            ret.append(item)
        return ret