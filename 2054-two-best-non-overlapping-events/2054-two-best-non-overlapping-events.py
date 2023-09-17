import heapq
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
    	q, cur, ans = [], 0, 0
    	for s, e, v in sorted(events):
	    	while(q and q[0][0]<s):
	    		cur = max(cur, heappop(q)[1])
	    	ans = max(ans, cur+v)
	    	heappush(q, (e, v))
    	return ans