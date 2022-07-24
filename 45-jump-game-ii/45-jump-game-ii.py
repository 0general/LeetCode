from collections import deque
class Solution:
    def jump(self, nums: List[int]) -> int:
        x = len(nums)
        visited = [x for _ in range(x)]
        visited[0] = 0
        q = deque()
        q.append(0)
        while q:
            n = q.popleft()
            for i in range(1,nums[n]+1):
                if n+i >= x or visited[n+i] <= visited[n] + 1:
                    continue
                visited[n+i] = visited[n] + 1
                q.append(n+i)
        
        return visited[x-1]
        
        
        