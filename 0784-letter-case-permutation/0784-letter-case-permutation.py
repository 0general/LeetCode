class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        check = set()
        def bt(idx, string):
            nonlocal s, check
            if idx > len(s):
                return
            if idx == len(s):
                check.add(string)
                return
            x = ord(s[idx])
            if 65 <= x < 91:
                bt(idx+1, string+chr(x+32))
            if 97 <= x < 123:
                bt(idx+1, string+chr(x-32))
            bt(idx+1, string+s[idx])
        bt(0, "")
        return list(check)
        
        
                
        