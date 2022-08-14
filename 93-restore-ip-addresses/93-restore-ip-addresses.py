class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12:
            return []
        
        ans = []
        
        def bt(i,dots,ip):
            if dots == 4 and i == len(s):
                ans.append(ip[:-1]) # '.'제거
                return
            if dots > 4:
                return
            
            for k in range(i, min(i+3,len(s))):
                if int(s[i:k+1]) <= 255 and (i == k or s[i] != "0"):
                    bt(k+1,dots+1,ip+s[i:k+1]+'.')
       
        bt(0,0,"")
        return ans