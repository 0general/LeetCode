import heapq
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        mod = int(1e9) + 7
        # zip을 이용하는 방법 solution 참고
        es_ls = list(zip(efficiency, speed))
        es_ls.sort(key=lambda x : -x[0])
        max_eff, sum_speed = 0, 0
        h = []
        for e,s in es_ls: # e가 큰 순으로 들어옴
            if len(h) == k:
                sum_speed -= heappop(h)
            heappush(h,s)
            sum_speed += s
            max_eff = max(max_eff, sum_speed*e)
        return max_eff % mod
            
            