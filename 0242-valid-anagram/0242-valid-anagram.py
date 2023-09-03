class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        al = [0] * 26
        for letter in s:
            al[ord(letter)-97] += 1
        for letter in t:
            num = ord(letter) - 97
            if al[num]:
                al[num] -= 1
            else:
                return False
        if sum(al):
            return False
        return True
        