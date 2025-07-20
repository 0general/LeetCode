class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        # https://leetcode.com/problems/smallest-integer-divisible-by-k/solutions/1655732/c-java-python-5-lines-image-explain-beginner-friendly/
        hit, n , ans = [False] * k, 0, 0
        while True:
            ans, n = ans + 1, (n * 10 + 1) % k
            if n == 0: return ans
            if hit[n]: return -1
            hit[n] = True