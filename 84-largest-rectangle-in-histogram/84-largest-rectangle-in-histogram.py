class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        n = len(heights)
        mn = [(0,n)] # 높이, index
        mx = 0
        for i in range(len(heights)-1,-1,-1):
            while mn:
                if mn[-1][0] and mn[-1][0] >= heights[i]:
                    top,_ = mn.pop()
                    if mn:
                        mx = max(mx, top*(mn[-1][1]-(i+1)))
                else:
                    break
            if mn:
                mx = max(mx,heights[i]*(mn[-1][1]-i))
            mn.append((heights[i],i))
        while mn:
            top, _ = mn.pop()
            if top:
                mx = max(mx,top*(mn[-1][1]))
        return mx
            
            
           
                    
                
        