class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # sliding window
        # 참고 : https://leetcode.com/problems/count-number-of-nice-subarrays/discuss/419378/JavaC%2B%2BPython-Sliding-Window-O(1)-Space
        left = count = res = 0
        for right in range(len(nums)):
            if nums[right] % 2:
                k -= 1
                count = 0
            while k == 0:
                k += nums[left] % 2
                left += 1
                count += 1
            res += count
        return res