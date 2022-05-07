import heapq
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: (x[1],x[2]))
        g = [0]*capacity
        heapq.heapify(g)
        for t in trips:
            for x in range(t[0]):
                if g[0] <= t[1]:
                    heapq.heappop(g)
                    heapq.heappush(g,t[2])
                else:
                    return False
                                
        return True
                
            
        