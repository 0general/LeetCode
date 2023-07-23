from collections import Counter
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        ls = sorted(Counter(nums).items(), key=lambda x : (x[1], -x[0]))
        result = []
        for key, value in ls:
            result.extend([key]*value)
        return result