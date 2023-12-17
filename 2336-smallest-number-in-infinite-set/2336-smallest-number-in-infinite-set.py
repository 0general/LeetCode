import heapq
class SmallestInfiniteSet:
    h = []
    dic = set()

    def __init__(self):
        self.h = [i for i in range(1,1001)]
        self.dic = set([i for i in range(1, 1001)])
        heapq.heapify(self.h)
        
    def popSmallest(self) -> int:
        x = heapq.heappop(self.h)
        self.dic.remove(x)
        if x >= 1000:
            heapq.heappush(self.h, x+1)
            self.dic.add(x)
        return x   

    def addBack(self, num: int) -> None:
        if num not in self.dic:
            heapq.heappush(self.h, num)
            self.dic.add(num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)