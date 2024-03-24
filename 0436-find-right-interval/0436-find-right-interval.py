class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        length = len(intervals)
        ans = [-1] * length
        sl = sorted([[v[0], v[1], idx] for idx, v in enumerate(intervals)])
        
        def bs(x): # x보다 크거나 같은 가장 작은 start를 가진 idx 구하기
            nonlocal sl
            s, e = 0, length - 1
            dap = length
            while s <= e:
                mid = (s + e) // 2
                if sl[mid][0] >= x:
                    dap = sl[mid][2]
                    e = mid - 1
                else:
                    s = mid + 1
            return dap
        
        for _, j, k in sl:
            idx = bs(j)
            
            if idx < length:
                ans[k] = idx
        
        return ans