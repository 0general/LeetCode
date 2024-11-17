from collections import Counter
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        length = len(goal)
        cnt = Counter(goal)
        if (length == len(s) and cnt == Counter(s)):
            target = min(cnt, key = cnt.get)
            x = goal.find(target)
            goal_string = goal[x:] + goal[:x]
            idx = 0
            while True:
                idx = s.find(target, idx)
                if idx > -1:
                    if (s[idx:] + s[:idx] == goal_string):
                        return True
                    idx += 1
                    continue
                return False
        return False
        