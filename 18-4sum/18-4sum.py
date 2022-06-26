class Solution:
    def two_sum(self, nums:List[int], target:int, output:set, num1:int, num2:int):
        hashmap = dict()
        for num in nums:
            if target-num in hashmap:
                output.add(tuple(sorted([target-num,num,num1,num2])))
            hashmap[num] = True
        
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        output = set() # python 3.6 부터는 입력 순서 보장
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                x = nums[i]+nums[j]
                
                self.two_sum(nums[j+1:],target-x,output,nums[i],nums[j])
                
        
        return list(output)
                            
                    
        