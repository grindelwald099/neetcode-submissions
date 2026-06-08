class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        arr=[]
        for i in range(0,len(heights)):
            sum=heights[i]
            for j in range(i+1,len(heights)):
                if i==(len(heights)-1):
                    break
                if heights[j] >= heights[i]:
                    sum+=heights[i]
                else:
                    break
            for j in range(i-1,-1,-1):
                if i==0:
                    break
                if heights[j] >= heights[i]:
                    sum+=heights[i]
                else:
                    break
            arr.append(sum)
        arr.sort(reverse=True)
        return arr[0]
