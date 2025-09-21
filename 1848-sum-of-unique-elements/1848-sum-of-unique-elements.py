class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        add_target = set()
        delete_target = set()
        for num in nums:
            if num not in add_target:
                add_target.add(num)
            else:
                delete_target.add(num)
        return sum(add_target - delete_target)