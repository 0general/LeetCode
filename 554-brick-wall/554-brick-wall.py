class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        num = defaultdict(int)
        num[0] = 0
        for i in range(len(wall)):
            for j in range(len(wall[i])-1):
                if j == 0:
                    num[wall[i][j]] += 1
                else:
                    wall[i][j] += wall[i][j-1]
                    num[wall[i][j]] += 1
        x = sorted(set(num.values()), reverse=True)
        return len(wall)-x[0]                
        