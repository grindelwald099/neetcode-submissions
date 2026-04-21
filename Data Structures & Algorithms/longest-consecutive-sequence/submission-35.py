class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cnt=1
        val=[]
        nums=sorted(nums, reverse=True)
        nums = list(dict.fromkeys(nums))
        k=1
        if(len(nums)>1):
            for i in range(0,(len(nums)-1)):
                if((nums[i] - nums[i+1])==1):
                    k=0
                if((k==0) and ((nums[i] - nums[i+1])==1)):
                    cnt+=1
                else:
                    cnt=1
                    k=1
                val.append(cnt)
                
            val=sorted(val, reverse=True)
            return (val[0])
        else:
            if (len(nums)==1):
                return 1
            else:
                return 0