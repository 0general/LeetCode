class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        ans = []
        nums.sort()
        temp = []
        for i in range (len(nums)//3):
            x = i * 3
            if (nums[x+2] - nums[x] > k):
                return []
            else:
                ans.append(nums[x:x+3])
        return ans
