from collections import Counter
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        cnt = dict(Counter(moves))
        for s in ['L', 'R', 'U', 'D']:
            if s not in cnt:
                cnt[s] = 0
        if cnt['L'] == cnt['R'] and cnt['U'] == cnt['D']:
            return True
        return False