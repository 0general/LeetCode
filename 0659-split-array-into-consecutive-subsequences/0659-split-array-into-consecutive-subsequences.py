from collections import defaultdict, Counter
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        sub = defaultdict(int)
        cnt = Counter(nums)
        
        for num in nums:
            if not cnt[num]:
                continue
            if sub[num-1] > 0:
                sub[num-1] -= 1
                sub[num] += 1
            else:
                if not cnt[num+1] or not cnt[num+2]:
                    return False
                cnt[num+1] -= 1
                cnt[num+2] -= 1
                sub[num+2] += 1
            cnt[num] -= 1
        return True