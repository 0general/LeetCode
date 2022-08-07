class StockSpanner:

    def __init__(self):
        self.stack = []
        self.idx = 0

    def next(self, price: int) -> int:
        self.idx += 1
        while self.stack:
            if self.stack[-1][0] <= price:
                self.stack.pop()
            else:
                break
        ans = self.idx
        if len(self.stack):
            ans -= self.stack[-1][1]
        self.stack.append((price,self.idx))
        return ans
        
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)