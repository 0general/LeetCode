class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        id = n
        time = [0] * n
        mx = 0
        start = 0
        for i, lt in logs:
            time[i] = max(time[i], lt-start)
            start = lt
            if (time[i] > mx) or (time[i] == mx and i < id):
                id = i
                mx = time[i]
        return id
        