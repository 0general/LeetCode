from collections import Counter

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        return Counter(arr).most_common()[0][0]
        