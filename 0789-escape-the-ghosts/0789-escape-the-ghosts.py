class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        # 유령보다 목적지에 일찍 도착할 수 없으면 실패
        min_length = abs(target[0]) + abs(target[1])
        for i, j in ghosts:
            if abs(target[0] - i) + abs(target[1] - j) <= min_length:
                return False
        return True