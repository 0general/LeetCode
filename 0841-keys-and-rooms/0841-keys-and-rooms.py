class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        not_visited = [1] * len(rooms)
        ls = set()
        not_visited[0] = 0
        ls.update(rooms[0])
        while ls:
            x = ls.pop()
            if not_visited[x]:
                not_visited[x] = 0
                ls.update([i for i in rooms[x] if not_visited[i]])
        return sum(not_visited) == 0
        