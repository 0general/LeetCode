class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 1:
            return n
        
        # 오른쪽부터 최소값을 저장하는 배열
        min_right = [0] * n
        min_right[-1] = arr[-1]
        for i in range(n - 2, -1, -1):
            min_right[i] = min(arr[i], min_right[i + 1])

        max_left = -math.inf
        chunks = 0
        
        # arr[i]까지 보면 현재 max_left, 만약 max_left <= min_right[i+1]라면
        # i에서 청크를 쪼갤 수 있음
        for i in range(n - 1):
            max_left = max(max_left, arr[i])
            if max_left <= min_right[i + 1]:
                chunks += 1
        
        return chunks + 1