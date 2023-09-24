class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:

        acc, toggle = [0]*len(nums), 0

        for idx, num in enumerate(nums):
            if idx >= k: toggle ^= acc[idx - k]

            if toggle != num: continue

            if k > len(nums) - idx: return -1

            toggle ^= 1
            acc[idx] = 1

        return sum(acc)