from collections import deque
# https://leetcode.com/problems/longest-binary-subsequence-less-than-or-equal-to-k/discuss/3081305/Python-or-One-Pass-%2B-deque-or-O(n) 참고
class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        zero_num = 0
        q = deque()
        for num in s:
            q.append(num)
            while q and q[0] == "0":
                zero_num += 1
                q.popleft()
            if q and int("".join(q), 2) > k:
                q.popleft()
        return zero_num + len(q)