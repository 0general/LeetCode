class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        # 가중치 중앙값 이용 케이스 참고 
        # https://leetcode.com/problems/minimum-cost-to-make-array-equal/discuss/2734183/Python3-Weighted-Median-O(NlogN)-with-Explanations
        arr = sorted(zip(nums, cost))
        total, cnt = sum(cost), 0
        for num, c in arr:
            cnt += c
            if cnt > total // 2:
                target = num
                break
        return sum(c * abs(num - target) for num, c in arr)