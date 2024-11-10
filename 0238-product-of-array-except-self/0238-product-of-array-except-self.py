class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        r_nums = list(reversed(nums))
        n = len(nums)
        for i in range(1, n):
            nums[i] *= nums[i - 1]
            r_nums[i] *= r_nums[i - 1]
        print(nums)
        print(r_nums)
        answer = []
        for i in range(n):
            x = 1
            if i != 0:
                x *= nums[i - 1]
            if i != n-1:
                x *= r_nums[n - i - 2]
            answer.append(x)
        return answer