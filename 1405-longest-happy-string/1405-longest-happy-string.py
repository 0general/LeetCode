class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        dic = [[a, "a"], [b, "b"], [c, "c"]]
        ans = ""
        while True:
            dic.sort()
            i = 2
            if len(ans) >= 2 and ans[-1] == ans[-2] == dic[2][1]:
                i = 1
            if dic[i][0]:
                ans += dic[i][1]
                dic[i][0] -= 1
            else:
                break
        return ans