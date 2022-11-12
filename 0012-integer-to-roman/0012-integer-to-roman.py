class Solution:
    def intToRoman(self, num: int) -> str:
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        sym = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        
        ans = ''
        i = 0
        while num and i < len(nums):
            if nums[i] > num:
                i += 1
                continue
            x = num//nums[i]
            ans += sym[i]*x
            num -= nums[i]*x
            i += 1
        return ans