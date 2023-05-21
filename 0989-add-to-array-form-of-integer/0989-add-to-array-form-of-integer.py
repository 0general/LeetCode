class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        carry = 0
        result = []
        i = len(num) - 1
        while i >= 0 or carry or k:
            sum = k % 10 + carry
            if i >= 0 : sum += num[i]
            carry = sum // 10
            k //= 10
            result.append(sum % 10)
            i -= 1
            
        return reversed(result)