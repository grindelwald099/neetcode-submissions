class Solution:
    def maxArea(self, heights: List[int]) -> int:
        arr=[]
        for i in range(len(heights)):
            for j in range(len(heights)):
                temp=0
                if i==j:
                    continue
                else:
                    temp=abs(j-i)*min(heights[i],heights[j])
                    arr.append(temp)
        arr=sorted(arr,reverse=True)
        return arr[0]



        