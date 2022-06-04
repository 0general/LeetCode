class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        arr = [[s[0],1]]
        # 스택 이용
        for i in range(1,len(s)):
            if arr and s[i] == arr[-1][0]:
                arr[-1][1] += 1
            else:
                arr.append([s[i],1])
            if arr[-1][1] == k:
                arr.pop()
        
        return ''.join([i[0]*i[1] for i in arr])
            
        