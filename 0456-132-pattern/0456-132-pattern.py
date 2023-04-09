from collections import deque
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        stack = [] # 가장 큰 수가 맨 위로
        comp = -1e9-1
        for num in nums[::-1]:
            if comp > num: # 큰 수 중에 제일 작은 수 보다 작은 수가 존재
                return True
            
            while stack and stack[-1] < num:
                comp = stack.pop() # 큰 수 중에 가장 작은 수 저장
            stack.append(num)
        
        return False
