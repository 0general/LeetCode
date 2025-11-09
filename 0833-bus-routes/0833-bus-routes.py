from collections import defaultdict, deque

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        stop_to_routes = defaultdict(set)
        for i, r in enumerate(routes):
            for stop in r:
                stop_to_routes[stop].add(i)
        visited_routes = set()
        visited_stops = set([source])
        queue = deque()
        for route in stop_to_routes[source]:
            queue.append((route, 1))
            visited_routes.add(route)
        while queue:
            route, buses = queue.popleft()
            for stop in routes[route]:
                if stop == target:
                    return buses
                if stop in visited_stops:
                    continue
                visited_stops.add(stop)
                for next_route in stop_to_routes[stop]:
                    if next_route not in visited_routes:
                        visited_routes.add(next_route)
                        queue.append((next_route, buses + 1))
        return -1