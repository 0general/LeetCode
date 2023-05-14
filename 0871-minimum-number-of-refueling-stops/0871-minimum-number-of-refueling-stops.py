import heapq
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        fuel = startFuel # 현재 가지고 있는 연료
        cnt, prev = 0, 0 # 연료 충전 횟수, 이전 위치
        stations.append([target, 0])
        miss = []
        
        for pos, gas in stations:
            dis, prev = pos - prev, pos # 거리 계산
            
            if fuel < dis: # 해당 위치까지 도달할 수 없는 경우
                while miss and fuel < dis:
                    fuel += -heapq.heappop(miss) # 가장 많은 양부터 합
                    cnt += 1 # 주유 횟수
                
                if fuel < dis: return -1 # 모두 주유했음에도 도달 불가
                
            fuel -= dis # 해당 위치까지 도달하기 위해 사용한 양
            heapq.heappush(miss, -gas)
            
        return cnt