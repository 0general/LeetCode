class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        work = {}
        today = 0
        for task in tasks:
            today += 1
            if task in work:
                today = max(work[task] + space + 1, today)
            work[task] = today
        return today
        