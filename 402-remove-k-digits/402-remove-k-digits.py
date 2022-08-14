class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k == 0:
            return num
        if num == "":
            return "0"
        stack = []
        length = len(num)
        for i in range(length):
            if k == 0:
                stack.append(num[i:])
                break
            while stack and k and int(stack[-1]) > int(num[i]):
                stack.pop()
                k -= 1
            stack.append(num[i])
        while k:
            stack.pop()
            k -= 1
        if len(stack) == 0:
            return '0'
        return str(int(''.join(stack)))