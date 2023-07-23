class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        # 참고 : https://leetcode.com/problems/letter-tile-possibilities/discuss/308392/4-lines-python-set-solution
        res ={''}
        for tile in tiles:
            res |= {s[:i] + tile + s[i:] for s in res for i in range(len(s) + 1)}
        return len(res) - 1