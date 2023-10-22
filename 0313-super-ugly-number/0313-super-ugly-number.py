import heapq
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        h = [(prime, prime, 1) for prime in primes]
        ls = [1]
        heapq.heapify(h)
        for _ in range(n-1):
            ls.append(h[0][0])
            while h[0][0] == ls[-1]:
                num, prime, idx = heapq.heappop(h)
                heapq.heappush(h, (prime*ls[idx], prime, idx + 1))
        return ls[-1]
        