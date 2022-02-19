import heapq

class MedianFinder:

    def __init__(self):
        self.small = []
        self.big = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small,-num) # 최대 힙
        heapq.heappush(self.big,-heapq.heappop(self.small)) # 최소 힙
        
        # 최대 힙에는 항상 최소 힙보다 작거나 같은 숫자만 남겨야 한다.
        if len(self.big) > len(self.small):
            heapq.heappush(self.small, -heappop(self.big))
              
        

    def findMedian(self) -> float:
        if len(self.small) > len(self.big):
            return -self.small[0]
        else:
            return (self.big[0]-self.small[0])/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()