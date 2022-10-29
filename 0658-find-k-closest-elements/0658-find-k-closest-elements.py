from collections import deque
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        ls = [] 
        for num in arr:
            ls.append((num, abs(x - num)))
                      
        ans = []
        for idx in sorted(ls, key = lambda x: x[1]):
            k -= 1
            ans.append(idx[0]) 
            if k == 0: 
                break
        return sorted(ans)
                
        