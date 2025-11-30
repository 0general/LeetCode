from itertools import combinations

class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)
        masks = []
        # 모든 부분수열 mask 생성 (1..(1<<n)-1)
        for mask in range(1, 1 << n):
            subseq = []
            for i in range(n):
                if (mask >> i) & 1:
                    subseq.append(s[i])
            t = "".join(subseq)
            if t == t[::-1]:  # palindrome 체크
                masks.append((mask, len(t)))
        # 가능한 두 개의 disjoint palindrome 조합 탐색
        best = 0
        m = len(masks)
        for i in range(m):
            mask1, len1 = masks[i]
            for j in range(i + 1, m):
                mask2, len2 = masks[j]
                if mask1 & mask2 == 0:
                    best = max(best, len1 * len2)
        return best