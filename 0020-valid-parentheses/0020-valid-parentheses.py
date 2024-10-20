class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {")":"(", "}":"{", "]":"["}
        for c in s:
            if c in pair.keys():
                if stack and stack[-1] == pair[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        if stack:
            return False
        return True