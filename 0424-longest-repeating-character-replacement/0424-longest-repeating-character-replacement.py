from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # https://leetcode.com/problems/longest-repeating-character-replacement/discuss/2524523/Easy-oror-100-oror-Fully-Explained-oror-C%2B%2B-Java-Python-JavaScript-Python3-oror-Sliding-Window
        maxCount, maxLength = 0, 0
        clc = Counter()
        for idx, val in enumerate(s):
            clc[val] += 1
            maxCount = max(maxCount, clc[val])
            if maxLength - maxCount >= k:
                clc[s[idx-maxLength]] -= 1
            else:
                maxLength += 1
        return maxLength
            
        