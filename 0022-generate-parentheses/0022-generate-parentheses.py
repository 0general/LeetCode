class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        arr = []
        def bt(n, string, remain_open):
            nonlocal arr
            if n == 0:
                if remain_open == 0:
                    arr.append(string)
                return
            if remain_open < n:
                bt(n, string+"(",remain_open+1)
            if remain_open:
                bt(n-1,string+")",remain_open-1)
            return
        
        bt(n, "", 0)
        
        return arr