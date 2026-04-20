class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        bool = False
        for i in range(0,(len(nums)-1)):
            ch=0
            ch=nums[i]
            k=0
            for j in ((i+1),len(nums)-1):
                if (nums[j]==ch):  
                    k=1
            if (k==1):
                bool = True
                break
        return bool
              