class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        def square(a):
            return a**2
        
        return sorted(map(square, nums))
        