class Solution:
    def isSymmetric(self, x):
        num = str(x)
        length = len(num)
        if length % 2:
            return False
        left = num[:length//2]
        right = num[length//2:]
        return sum(map(int, left)) == sum(map(int, right))
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        result = 0
        for x in range(low, high + 1):
            result += self.isSymmetric(x)
        return result
        