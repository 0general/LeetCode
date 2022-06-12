class FreqStack:

    def __init__(self):
        self.dict = defaultdict(int)
        self.stack = defaultdict(list)
        self.max_freq = 0
        
    def push(self, val: int) -> None:
        # val의 빈도수 갱신
        self.dict[val] += 1
        self.stack[self.dict[val]].append(val)
        self.max_freq = max(self.max_freq, self.dict[val])

    def pop(self) -> int:
        m = self.max_freq
        max_freq_list = self.stack[m]
        ans = max_freq_list[-1]
        max_freq_list.pop()
        self.dict[ans] -= 1
        while len(self.stack[self.max_freq]) == 0 and self.max_freq:
            self.max_freq -= 1
        
        return ans
            
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()