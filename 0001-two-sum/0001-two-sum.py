class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        ls = [(i,nums[i]) for i in range(n)]
        ls.sort(key=lambda x : x[1])
        s, e = 0, n-1
        while s < e:
            t = target - ls[s][1]
            l, r = s + 1, e
            while l <= r:
                mid = (l+r)//2
                if ls[mid][1] == t:
                    return [ls[s][0], ls[mid][0]]
                elif ls[mid][1] > t:
                    r = mid - 1
                    e = mid - 1
                else:
                    l = mid + 1
            s += 1
        
        