import heapq
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        # 참고 : https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/discuss/2560020/Min-Heap
        pq = []
        for left, right in sorted(intervals): # 작은 순으로 정렬
            if pq and pq[0] < left: # 겹치지 않으면
                heapq.heappop(pq) # 다음 비교구간으로 교체 저장
            heapq.heappush(pq, right)
        return len(pq)