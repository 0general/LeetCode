from collections import deque
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        
        def change(a):
            if a > 0:
                return 'R'
            elif a == 0:
                return '.'
            else:
                return 'L'
            
        
        length = len(dominoes)
        
        balance = [0]*length
        visited = [False]*length
        
        q = deque()
        for i in range(length):
            if dominoes[i] == 'R':
                visited[i] = True
                q.append(i)
                balance[i] = 1
            elif dominoes[i] == 'L':
                visited[i] = True
                q.append(i)
                balance[i] = -1
        
        while q:
            now = q.popleft()
            weight = balance[now]            
            if weight == 0:
                continue
            elif weight > 0:
                if now+1 >= length:
                    continue
                if not visited[now+1]:
                    visited[now+1] = True
                    balance[now+1] = weight + 1
                    q.append(now+1)
                elif balance[now+1] + weight + 1 == 0:
                    balance[now+1] = 0
            else:
                if now-1 < 0:
                    continue
                if not visited[now-1]:
                    visited[now-1] = True
                    balance[now-1] = weight - 1
                    q.append(now-1)
                elif balance[now-1] + weight - 1 == 0:
                    balance[now-1] = 0
        
        
        return ''.join(list(map(change,balance)))   