class Solution:
    parent = {}
    
    def find_parent(self,a):
        if self.parent[a] != a:
            self.parent[a] = self.find_parent(self.parent[a])
        return self.parent[a]
        
    def longestConsecutive(self, nums: List[int]) -> int:
        number = {}
        
        for num in nums:
            number[num] = 1
            if number.get(num-1,0): # parent 바꿔주기
                self.parent[num] = self.find_parent(num-1)
            else:
                self.parent[num] = num
            if number.get(num+1,0): # 집합을 합치는 역할
                self.parent[num+1] = self.parent[num]
        
        ans = 0
        for num in nums:
            ans = max(ans, num - self.find_parent(num)+1)
        
        return ans
        
        
        