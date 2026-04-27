class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        arr=[]
        i=0
        j=k
        while(i<len(nums)-k+1):
            temp=[]
            temp=nums[i:j]
            temp=sorted(temp,reverse=True)
            arr.append(temp[0])
            i+=1
            j+=1
        return arr

        