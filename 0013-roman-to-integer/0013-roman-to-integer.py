class Solution:
    def romanToInt(self, s: str) -> int:
        nums = {"I": 1, 'IV': 4,	'V': 5, 'IX':9, 'X': 10, 'XL': 40, 'L': 50, 'XC':90, 'C': 100, 'CD':400, 'D': 500, 'CM':900, 'M': 1000}
        answer = 0
        rome_num = ""
        for i in s[::-1]:
            if rome_num and nums[rome_num] > nums[i]:
                answer += nums[i + rome_num]
                rome_num = ""
            else:
                if rome_num != "":
                    answer += nums[rome_num]
                rome_num = i
        if rome_num:
            answer += nums[rome_num]
        return answer
            