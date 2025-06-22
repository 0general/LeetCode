class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s = str(num)
        return sum(int(s[i:i+k]) != 0 and num % int(s[i:i+k]) == 0 for i in range(len(s) - k + 1))