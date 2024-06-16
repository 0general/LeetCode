from collections import defaultdict
class MagicDictionary:

    def __init__(self):
        self.dic = defaultdict(int)
        self.real = defaultdict(int)
        
    def _cal_list(string):
        ans = set()
        for i in range(len(string)):
            ans.add(string[:i] + "*" + string[i+1:])
        return list(ans)
        
    def buildDict(self, dictionary: List[str]) -> None:
        for st in dictionary:
            self.real[st] += 1
            for s in MagicDictionary._cal_list(st):
                self.dic[s] += 1
        

    def search(self, searchWord: str) -> bool:
        check = self.real[searchWord]
        for s in MagicDictionary._cal_list(searchWord):
            if check == 0 and self.dic[s] > 0: return True
            elif check > 0 and self.dic[s] > 1: return True
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)