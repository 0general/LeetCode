class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        # 가장 작은 페널티 값 찾기
        left, right = 1, max(nums)
        while left < right:
            mid = (left + right) // 2
            if (sum((num - 1) // mid for num in nums) > maxOperations):
                left = mid + 1
            else:
                right = mid
        return left
