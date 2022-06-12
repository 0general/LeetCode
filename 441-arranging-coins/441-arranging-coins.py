class Solution:
    def arrangeCoins(self, n: int) -> int:
        s,e = 0, n
        ans = 0
        while s <= e:
            mid = (s+e)//2
            if (mid*(mid+1))//2 <= n:
                ans = mid
                s = mid + 1
            else:
                e = mid - 1
        return ans
                