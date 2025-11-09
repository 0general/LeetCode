class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        n = len(nums)
        if n == 0:
            return ans
        start = nums[0]
        for i in range(1, n + 1):
            if i == n or nums[i] != nums[i - 1] + 1:
                end = nums[i - 1]
                if start != end:
                    ans.append(f"{start}->{end}")
                else:
                    ans.append(str(start))
                if i < n:
                    start = nums[i]
        return ans