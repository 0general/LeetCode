class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        else:
            rs = s[::-1]
            n = len(s)
            for i in range(n//2):
                if s[i] != s[-i-1]:
                    x = s[i+1:n-i]
                    if x == x[::-1]:
                        return True
                    x = s[i:n-i-1]
                    if x == x[::-1]:
                        return True  
                    return False
            return False
                    
        