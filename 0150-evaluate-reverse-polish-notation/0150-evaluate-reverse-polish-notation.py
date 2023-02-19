class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for token in tokens:
            if token == "+":
                num2 = nums.pop()
                num1 = nums.pop()
                nums.append(num1+num2)
            elif token == "-":
                num2 = nums.pop()
                num1 = nums.pop()
                nums.append(num1-num2)
            elif token == "*":
                num2 = nums.pop()
                num1 = nums.pop()
                nums.append(num1*num2)
            elif token == "/":
                num2 = nums.pop()
                num1 = nums.pop()
                nums.append(int(num1/num2))
            else:
                nums.append(int(token))
        return nums[0]
        