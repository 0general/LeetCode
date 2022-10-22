class MyCircularQueue:

    def __init__(self, k: int):
        self.q = ['' for _ in range(k)]
        self.front = k-1
        self.rear = 0
        self.size = 0
        self.full = k

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        self.q[self.rear] = value
        self.rear += 1
        self.size += 1
        if self.rear == self.full:
            self.rear = 0
        return True
        
    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        self.front = (self.front + 1)%self.full
        self.size -= 1
        return True
        
    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.q[(self.front + 1)%self.full]
        

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.q[self.rear - 1]
        

    def isEmpty(self) -> bool:
        if self.size : 
            return False
        return True

    def isFull(self) -> bool:
        if self.size == self.full:
            return True
        return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()