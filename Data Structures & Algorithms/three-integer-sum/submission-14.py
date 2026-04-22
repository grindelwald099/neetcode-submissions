class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arr=[]
        nums=sorted(nums,reverse=False)
        k=0
        for i in range(0,len(nums)):
            sum=0
            l=0
            r=0
            l=i+1
            r=len(nums)-1
            if nums[i]<=0:
                 while(l<r):
                    sum=nums[i]+nums[l]+nums[r]
                    if sum==0:
                        arr.append([nums[i] , nums[l] , nums[r]])
                        l=l+1
                    elif sum<0:
                        l+=1
                    else:
                        r=r-1
        arr2=[]
        temp=[]
        for ch in arr:
            temp.append(tuple(ch))
        temp=set(temp)
        for ch in temp:
            arr2.append(ch)
        return arr2
                


        