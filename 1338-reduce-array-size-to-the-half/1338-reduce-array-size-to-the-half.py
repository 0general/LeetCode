from collections import defaultdict
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        numbers = defaultdict(int)
        for num in arr:
            numbers[num] += 1
        length = len(arr) / 2
        
        result = 0
        hap = 0
        for k, v in sorted(numbers.items(), key=lambda x: -x[1]):
            if hap >= length:
                return result
            hap += v
            result += 1
        return result
            
        