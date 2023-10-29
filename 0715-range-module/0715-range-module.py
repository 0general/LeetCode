from bisect import bisect_left as bl, bisect_right as br
class RangeModule:

    # Discuss 참고
    def __init__(self):
        self.track = []

    def addRange(self, left: int, right: int) -> None:
        start = bl(self.track, left)
        end = br(self.track, right)
        
        self.track[start:end] = [left] * (start % 2 == 0) + [right] * (end % 2 == 0)
         

    def queryRange(self, left: int, right: int) -> bool:
        start = br(self.track, left)
        end = bl(self.track, right)
        if start == end and start % 2 == 1:
            return True
        return False
        

    def removeRange(self, left: int, right: int) -> None:
        start = bl(self.track, left)
        end = br(self.track, right)
        
        self.track[start:end] = [left] * (start % 2 == 1) + [right] * (end % 2 == 1)
        


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)