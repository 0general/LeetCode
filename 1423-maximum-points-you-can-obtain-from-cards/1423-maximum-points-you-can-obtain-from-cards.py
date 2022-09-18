class Solution:
    dic = dict()
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        idx = 0
        cur = len(cardPoints)-k
        currpoint = sum(cardPoints[cur:])
        ans = currpoint
        if cur == idx:
            return ans
        while cur < len(cardPoints):
            currpoint += cardPoints[idx] - cardPoints[cur]
            ans = max(ans, currpoint)
            idx += 1
            cur += 1
        return ans