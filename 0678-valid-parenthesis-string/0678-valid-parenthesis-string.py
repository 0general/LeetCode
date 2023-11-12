class Solution:
    def checkValidString(self, s: str) -> bool:
        left = 0
        for i in s:
            if i == "(" or i == "*":
                left += 1
            elif left > 0:
                left -=1
            else:
                return False
        right = 0
        
        for i in s[::-1]:
            if i == ")" or i == "*":
                right += 1
            elif right > 0:
                right -=1
            else:
                return False
        return True
        