class RandomizedSet:

    def __init__(self):
        self.mapping_dict = {}
        self.random_list = []
        

    def insert(self, val: int) -> bool:
        if val in self.mapping_dict:
            return False
        
        # 인덱스 저장
        self.mapping_dict[val] = len(self.random_list)
        self.random_list.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.mapping_dict:
            return False
        
        # 들어온 순서가 중요하지 않음. 제거할 숫자의 위치로 마지막 숫자를 옮기기
        change_target, remove_idx = self.random_list[-1], self.mapping_dict[val]
        self.mapping_dict[change_target] = remove_idx
        self.random_list[remove_idx] = change_target
        self.random_list.pop()
        del self.mapping_dict[val]
        
        return True

    def getRandom(self) -> int:
        return random.choice(self.random_list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()