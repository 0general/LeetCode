class Solution:
    def numSplits(self, s: str) -> int:
        ## https://leetcode.com/problems/number-of-good-ways-to-split-a-string/solutions/1520004/99-7-python-3-solution-with-17-lines-no-search-explained/
        length = len(s)
        if length == 1:
            return 0
        elif length == 2:
            return 1
        
        left, right = {}, {}

        for idx, c in enumerate(s):
            if c not in left:
                left[c] = idx
            right[c] = idx
        
        indices = list(left.values()) + list(right.values())
        indices.sort()

        middle = len(indices) // 2

        return indices[middle] - indices[middle - 1]