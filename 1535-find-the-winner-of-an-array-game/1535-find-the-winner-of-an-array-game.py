class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if len(arr) <= k : return max(arr)
        
        cnt = 0
        ans = arr[0]
        
        for x in arr[1:]:
            if x > ans:
                ans = x
                cnt = 1
            else:
                cnt += 1
            if cnt == k:
                break

        return ans