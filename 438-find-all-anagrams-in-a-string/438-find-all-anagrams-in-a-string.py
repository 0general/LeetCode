class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        alpha = dict()
        for x in p:
            alpha[x] = alpha.get(x,0) + 1
        i = 0
        pl, sl = len(p), len(s)
        temp = dict()
        def check(temp):
            for x in temp:
                if alpha.get(x,0) != temp[x]:
                    return False
            return True
        num = 0
        while i < sl:
            if s[i] not in alpha:
                temp = dict()
                i += 1
                num = 0
                continue
            temp[s[i]] = temp.get(s[i],0) + 1
            num += 1
            if num > pl:
                temp[s[i-pl]] -= 1
                num -= 1
            i += 1
            if num == pl:
                if check(temp):
                    ans.append(i-pl)
        return ans
            
                
            