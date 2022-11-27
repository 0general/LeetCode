class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4:
            return False
        l = total // 4
        nums = []
        
        matchsticks.sort(reverse=True)
        length = [0]*4
        
        def BT(idx):
            if idx == len(matchsticks):
                return l == length[0] == length[1] == length[2]
            
            for i in range(4):
                if length[i] + matchsticks[idx] <= l:
                    length[i] += matchsticks[idx]
                    flag = BT(idx+1)
                    if flag:
                        return flag
                    length[i] -= matchsticks[idx]
                    
                    if length[i] == 0: # 끝까지 갔어도 채우지 못한다는 뜻
                        break
            return False
        
        return BT(0)
            
        
        
        
        