import heapq

class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        n = len(apples)
        pq = []  # min-heap storing (expire_day, remain_count)
        eaten = 0
        day = 0
        
        # 매일 또는 사과가 남아있을 동안 반복
        while day < n or pq:
            # 새로 자란 사과 추가
            if day < n and apples[day] > 0:
                expire = day + days[day]  # expire = day + days[day]
                heapq.heappush(pq, (expire, apples[day]))
            # 만료된 사과 제거
            while pq and pq[0][0] <= day:
                heapq.heappop(pq)
            # 사과 먹기 (가능하면)
            if pq:
                expire, count = heapq.heappop(pq)
                eaten += 1
                if count - 1 > 0:
                    heapq.heappush(pq, (expire, count - 1))
            day += 1
        
        return eaten