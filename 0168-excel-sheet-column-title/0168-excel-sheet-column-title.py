class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        while columnNumber > 0:
            columnNumber -= 1
            result += chr(columnNumber % 26 + ord("A"))
            columnNumber //= 26
        return result[::-1]
        