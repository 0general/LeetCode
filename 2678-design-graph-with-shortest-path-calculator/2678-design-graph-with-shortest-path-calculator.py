import heapq

class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.graph = [[] for _ in range(n)]
        for edge in edges:
            self.addEdge(edge)

    def addEdge(self, edge: List[int]) -> None:
        """
        새로운 directed weighted 간선 추가
        edge = [u, v, w]
        """
        u, v, w = edge
        self.graph[u].append((v, w))

    def shortestPath(self, node1: int, node2: int) -> int:
        """
        node1에서 node2로 가는 최단 경로 비용 반환
        경로가 없으면 -1.
        """
        # 거리 초기화
        dist = [float('inf')] * self.n
        dist[node1] = 0

        # (current_dist, node)
        heap = [(0, node1)]
        while heap:
            d, u = heapq.heappop(heap)
            # 이미 더 짧은 경로를 발견했으면 스킵
            if d > dist[u]:
                continue
            # 목적지에 도달하면 즉시 반환
            if u == node2:
                return d
            # 인접 간선 완화(relax)
            for v, w in self.graph[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(heap, (nd, v))

        return -1


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)