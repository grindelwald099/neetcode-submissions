class Solution:
    def trap(self, height: List[int]) -> int:
        max_left=[]
        max_right=[]
        temp1=[]
        temp2=[]
        for i in range(0,len(height)):
            for j in range(0,len(height)):
                if i==0:
                    temp1.append(0)
                if i==(len(height)-1):
                    temp2.append(0)
                if j<i:
                    temp1.append(height[j])
                elif j>i:
                    temp2.append(height[j])
                else:
                    continue
            temp1=sorted(temp1,reverse=True)
            temp2=sorted(temp2,reverse=True)
            max_left.append(temp1[0])
            max_right.append(temp2[0])
            temp1=[]
            temp2=[]
        check=[]
        for i in range(0,len(height)):
            check.append(min(max_left[i],max_right[i]))
        sum=0
        for i in range(len(height)):
            if ((-height[i]+check[i])>0):
                sum+=(-height[i]+check[i])
        return sum


                    


