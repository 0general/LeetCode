import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i in range(len(tasks)):
            tasks[i].append(i)
        tasks.sort(key=lambda x : (x[0],x[1],x[2]))
        time = 0
        idx = 0
        ans = []
        h = []
        while len(ans) < len(tasks):
            
            while idx < len(tasks) and time >= tasks[idx][0]:
                heapq.heappush(h,(tasks[idx][1],tasks[idx][2]))
                idx += 1
            if len(h):
                temp = []
                temp.append(heapq.heappop(h))
                while h and temp[0][0] == h[0][0]:
                    temp.append(heapq.heappop(h))
                temp.sort(key=lambda x : x[1])
                p, num = temp[0][0], temp[0][1]
                time += p
                ans.append(num)
                for i in range(1,len(temp)):
                    heapq.heappush(h,(temp[i]))
            if len(h)==0 and idx < len(tasks) and time < tasks[idx][0]:
                time = tasks[idx][0]
            
        return ans
        
            
            
        