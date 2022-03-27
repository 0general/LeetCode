class Solution:
    def longestPalindrome(self, s: str) -> str:
        # ref:https://sub2n.github.io/2019/04/22/LeetCode-5-Longest-Palindromic-Substring/
        # dp를 짜도 모든 substring에 대해 검사(O(n^2))하기 때문에 항상 시간초과가 난다. 
        # 아래 경우는 가장 긴 길이를 갱신할 수 있는가에 대한 여부만 검사하기 때문에 시간 초과가 안 난다.
        if len(s) <= 1:
            return s
        i,l=0,0 # 시작 인덱스와 길이를 저장
        for j in range(len(s)):
            if s[j-l: j+1] == s[j-l: j+1][::-1]:
                i, l = j-l, l+1
            elif j-l > 0 and s[j-l-1: j+1] == s[j-l-1: j+1][::-1]:
                i, l = j-l-1, l+2
        return s[i: i+l]