from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = Counter(s1)
        length = len(s1)
        match = len(counter)
        
        for i, ch in enumerate(s2):
            if ch in counter:
                counter[ch] -= 1
                if counter[ch] == 0:
                    match -= 1
            if i >= length and s2[i-length] in counter:
                if counter[s2[i-length]] == 0:
                    match += 1
                counter[s2[i-length]] += 1
            if match == 0:
                return True
        return False
        