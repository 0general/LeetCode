class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        length = len(arr)
        dp = [[2] * length for _ in range(length)]
        mapping = {v: i for i, v in enumerate(arr)}
        result = 2
        for i in range(length):
            for j in range(i+1, length):
                prev = arr[j] - arr[i]
                if prev >= arr[i]: break
                elif prev in mapping:
                    dp[i][j] = dp[mapping[prev]][i] + 1
                result = result if result > dp[i][j] else dp[i][j]
        if result > 2:
            return result
        return 0