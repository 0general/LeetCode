class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[0]-x[1])
        answer = 0
        
        x = len(costs)//2
        for i in range(x):
            answer += costs[i][0]
        for i in range(x,len(costs)):
            answer += costs[i][1]
        
        return answer