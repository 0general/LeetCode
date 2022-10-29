from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        element, num = Counter(nums).most_common(1)[0]
        if num > n//2:
            return element
        