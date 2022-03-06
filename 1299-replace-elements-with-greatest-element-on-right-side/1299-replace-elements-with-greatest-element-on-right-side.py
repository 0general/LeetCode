class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        mx = arr[-1]
        arr[-1] = -1
        for i in range(n-2,-1,-1):
            temp = arr[i]
            arr[i] = mx
            if temp > mx:
                mx = temp
        return arr
            
        