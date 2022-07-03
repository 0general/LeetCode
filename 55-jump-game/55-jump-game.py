import heapq
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        loc = 0 # 가능한 최대 위치
        for i in range(len(nums)):
            if i > loc: # 현재 위치가 가능한 최대 위치보다 크다면 실패
                return False
            loc = max(loc, i + nums[i])
            if loc >= len(nums)-1:
                break
        return True
        