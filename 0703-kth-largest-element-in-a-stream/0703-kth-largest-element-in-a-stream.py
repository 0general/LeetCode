class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = sorted(nums, reverse = True)[:k]
        self.k = k
        
    def add(self, val: int) -> int:
        if self.k == len(self.nums):
            if self.nums[-1] >= val:
                return self.nums[-1]
            else:
                temp = []
                for i in range(len(self.nums)):
                    if self.nums[i] > val:
                        temp.append(self.nums[i])
                    else:
                        temp.append(val)
                        temp.extend(self.nums[i:-1])
                        break
                self.nums = temp
                return self.nums[-1]
        else:
            if len(self.nums) == 0:
                self.nums.append(val)
                return self.nums[-1]
            if self.nums[-1] >= val:
                self.nums.append(val)
                return self.nums[-1]
            else:
                temp = []
                for i in range(len(self.nums)):
                    if self.nums[i] > val:
                        temp.append(self.nums[i])
                    else:
                        temp.append(val)
                        temp.extend(self.nums[i:])
                        break
                self.nums = temp
                return self.nums[-1]
                


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)