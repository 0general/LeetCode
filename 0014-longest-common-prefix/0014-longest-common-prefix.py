class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        for l in range(len(strs[0])):
            for idx in range(len(strs)):
                if l >= len(strs[idx]):
                    break
                if strs[0][l] != strs[idx][l]:
                    break
            else:
                ans += strs[0][l]
                continue
            break
        return ans
        