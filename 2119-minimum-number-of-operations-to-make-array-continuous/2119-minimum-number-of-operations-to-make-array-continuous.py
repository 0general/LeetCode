from bisect import bisect_right
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous/solutions/1470853/python-binary-search-clean-concise/
        n = len(nums)
        nums = sorted(set(nums))

        ans = n
        for i, start in enumerate(nums):
            end = start + n - 1
            idx = bisect_right(nums, end)
            uniqueLen = idx - i
            ans = min(ans, n - uniqueLen)
        return ans