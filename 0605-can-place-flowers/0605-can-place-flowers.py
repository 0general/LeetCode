class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        num = len(flowerbed)
        for i in range(num):
            if n == 0:
                return True
            if flowerbed[i]:
                continue
            if i == 0 and (i + 1) != num and not flowerbed[i+1]:
                flowerbed[i] = 1
                n -= 1
                continue
            if i == num-1 and not flowerbed[i-1]:
                flowerbed[i] = 1
                n -= 1
                continue
            if not flowerbed[i-1] and not flowerbed[i+1]:
                flowerbed[i] = 1
                n -= 1
                continue
        if n == 0:
            return True
        return False
            