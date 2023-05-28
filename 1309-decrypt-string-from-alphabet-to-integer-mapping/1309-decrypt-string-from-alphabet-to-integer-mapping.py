class Solution:
    def freqAlphabets(self, s: str) -> str:
        dic = dict()
        for i in range(1, 27):
            c = str(i)
            if i >= 10:
                c += "#"
            dic[c] = chr(96 + i)
        idx = len(s)-1
        result = ""
        while idx >= 0:
            if s[idx] == "#":
                c = s[idx-2:idx+1]
                result += dic[c]
                idx -= 3
            else:
                result += dic[s[idx]]
                idx -= 1
        return result[::-1]
        