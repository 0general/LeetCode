class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        ad = {chr(i): i - 97 for i in range(97, 123)}
        nd = {i: chr(97 + i) for i in range(26)}
        num = [0] * (len(s) + 1)
        for start, end, direction in shifts:
            if direction:
                num[start] += 1
                num[end + 1] -= 1
            else:
                num[start] -= 1
                num[end + 1] += 1
        
        for i in range(1, len(s)):
            num[i] += num[i - 1]
        return ''.join([nd[(ad[c] + num[i]) % 26] for i, c in enumerate(s)])