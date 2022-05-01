class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        # 이분탐색으로 가능할 듯
        s, e = max(nums), sum(nums)
        ans = e
        while s <= e:
            mid = (s+e)//2 # 가장 작은 최대 합
            n = 1
            temp = 0
            for i in nums:
                if temp + i <= mid:
                    temp += i
                else:
                    temp = i
                    n += 1
                if n > m:
                    s = mid + 1
                    break
            else:
                e = mid - 1
                ans = mid
        return ans
                
            
        