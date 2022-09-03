class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        dice_num = {}
        for i in range(len(tops)):
            dice_num[tops[i]] = dice_num.get(tops[i],0) + 1
            if tops[i] != bottoms[i]:
                dice_num[bottoms[i]] = dice_num.get(bottoms[i],0) + 1
            
            if max(dice_num.values()) < i + 1:
                return -1
        num = max(dice_num, key = dice_num.get)
        
        t, b = 0,0
        
        for i in range(len(tops)):
            if tops[i] != num:
                t += 1
            if bottoms[i] != num:
                b += 1
        
        return min(t,b)
        