class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def min_max(sum_, left, right, f_turn=True):
            if left == right:
                if f_turn:
                    return sum_ + nums[left]
                else:
                    return sum_ - nums[left]
            if f_turn:
                return max(min_max(sum_ + nums[left], left+1, right, False),
                           min_max(sum_ + nums[right], left, right - 1, False))
            else:
                return min(min_max(sum_ - nums[left], left+1, right, True),
                           min_max(sum_ - nums[right], left, right - 1, True))
        
        res = min_max(0, 0, len(nums) - 1)
        return res >= 0