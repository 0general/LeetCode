class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        def computetime(currpos, currtime):
            nonlocal target
            return (target-currpos)/currtime
        
        n = len(position)
        if n == 1:
            return 1
        arr = list(zip(position,speed))
        arr.sort(key=lambda x: (-x[0],-x[1]))
        # all the values of position are unique
        arrival_time = None
        ans = 0
        for i in range(n):
            curr_time = computetime(arr[i][0],arr[i][1]) # 도착하기까지 사용할 시간이 얼마나 걸리는지로 계산하는게 빠름
            if not arrival_time or curr_time > arrival_time:
                arrival_time = curr_time
                ans += 1
        return ans
        