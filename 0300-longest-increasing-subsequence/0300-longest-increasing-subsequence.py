class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        stack = []
        for num in nums:
            if not stack:
                stack.append(num)
                continue
            s, e = 0, len(stack) - 1
            temp = len(stack)
            while s <= e:
                mid = (s + e) // 2
                if stack[mid] >= num:
                    temp = mid
                    e = mid - 1
                else:
                    s = mid + 1
            if temp == len(stack):
                stack.append(num)
            else:
                stack[temp] = num        
        return len(stack)
        