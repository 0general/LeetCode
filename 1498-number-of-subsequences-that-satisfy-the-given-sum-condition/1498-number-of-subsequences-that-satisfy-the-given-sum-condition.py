class Solution:
    def __init__(self):
        self.num = 0
        self.MAX = int(1e9)+7
    
    def bs(self, start, nums, tg):
        s = start
        e = len(nums)-1
        ans = s
        while s <= e:
            mid = (s+e)//2
            if nums[mid] <= tg:
                ans = mid
                s = mid + 1
            else:
                e = mid - 1
        return ans-start
            
        
            
    def numSubseq(self, nums: List[int], target: int) -> int:
        power = [1]*len(nums)
        for i in range(1,len(power)):
            power[i] = (power[i-1]*2)%self.MAX
            
        nums.sort()
        for i in range(len(nums)):
            if nums[i]*2 > target:
                break
            # 이분 탐색으로 상한 인덱스 찾기
            self.num += power[self.bs(i,nums,target-nums[i])]
            self.num %= self.MAX
        
        return self.num
        