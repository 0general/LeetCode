from collections import defaultdict
import heapq
import math
class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        # 참고 : https://leetcode.com/problems/second-minimum-time-to-reach-destination/discuss/1525149/Python-Modified-Dijkstra-explained
        dim = [[] for _ in range(n+1)]
        dim[1] = [0]
        graph, h = defaultdict(list), [(0,1)]
        
        for u, v in edges:
            graph[u] += [v]
            graph[v] += [u]
            
        while h:
            dist, idx = heapq.heappop(h)
            if idx == n and len(dim[n]) == 2:
                return max(dim[n])
            for neib in graph[idx] :
                if (dist // change) % 2 == 0:
                    cand = dist + time
                else:
                    cand = math.ceil(dist/(2*change)) * (2*change) + time
                
                if not dim[neib] or (len(dim[neib]) == 1 and dim[neib] != [cand]):
                    dim[neib] += [cand]
                    heapq.heappush(h, (cand, neib))