   

class LRUCache:

    def __init__(self, capacity: int):
        self.dic = {}
        self.cap = capacity
        
    def get(self, key: int) -> int:
        if key not in self.dic: return -1
        val = self.dic[key]
        del self.dic[key]
        self.dic[key] = val
        return val
        
    def put(self, key: int, value: int) -> None:
        # 파이썬의 dictionary는 들어온 시간순으로 정렬을 유지한다.
        if key in self.dic:
            del self.dic[key]
        self.dic[key] = value
        if len(self.dic)>self.cap:
            for d in self.dic:
                del self.dic[d]
                break
        
                
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)