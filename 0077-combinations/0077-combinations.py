class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        
        def comb(num, ls):
            if len(ls) == k:
                result.append(ls)
                return
            if num > n or (k - len(ls)) > (n - num):
                return
            for i in range(num + 1, n + 1):
                comb(i, ls + [i])
        comb(0, [])
        return result