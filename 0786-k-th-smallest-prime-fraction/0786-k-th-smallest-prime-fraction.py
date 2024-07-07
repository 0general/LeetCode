import heapq
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        # 참고 : https://leetcode.com/problems/k-th-smallest-prime-fraction/discuss/5137672/Using-Heap-or-Python
        heap = []
        n = len(arr)
        for i in range(n-1):
            heapq.heappush(heap, (arr[i] / arr[-1], i, n-1))
        
        for i in range(k-1):
            res, l, r = heapq.heappop(heap)
            heapq.heappush(heap, (arr[l] / arr[r-1], l, r-1))

        res, l, r = heapq.heappop(heap)

        return [arr[l], arr[r]]
        