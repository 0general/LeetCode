class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dp = [-1]*(10**4+1)
        stack = []
        while nums2:
            x = nums2.pop()
            while stack:
                if stack[-1] < x:
                    stack.pop()
                else:
                    break
            if len(stack) == 0:
                dp[x] = -1
            else:
                dp[x] = stack[-1]
            stack.append(x)
        answer = []
        for num in nums1:
            answer.append(dp[num])
        return answer