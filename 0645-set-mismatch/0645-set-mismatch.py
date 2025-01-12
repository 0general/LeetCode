class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        h = dict(zip([i for i in range(1, n+1)], [0]*n))
        for num in nums:
            h[num] += 1
        sorted_dict = sorted(h.items(), key = lambda x: x[1], reverse = True)
        return [sorted_dict[0][0], sorted_dict[-1][0]]