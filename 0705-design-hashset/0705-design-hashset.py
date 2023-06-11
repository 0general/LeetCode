from collections import defaultdict 
class MyHashSet:
    def __init__(self):
        self.hs=defaultdict(bool)

    def add(self, key: int) -> None:
        self.hs[key] = True

    def remove(self, key: int) -> None:
        self.hs[key] = False

    def contains(self, key: int) -> bool:
        return self.hs[key]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)