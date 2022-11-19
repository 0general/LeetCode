class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # discuss/2781024 참고
        num = [0]*26
        x = ord('A')
        for task in tasks:
            num[ord(task)-x] += 1
        cnt = 0
        maxValue = max(num)
        for i in num:
            if i == maxValue:
                cnt += 1
        return max((n + 1)*(maxValue - 1)+cnt, len(tasks))
            
        
        