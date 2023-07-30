class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        length = len(nums)
        snums = map(str, nums)
        return length - sum(map(lambda x: len(x) % 2, snums))