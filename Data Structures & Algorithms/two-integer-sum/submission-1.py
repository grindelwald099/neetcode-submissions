class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr=[0] * 2
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i==j:
                    continue
                else:
                    if (nums[i]+nums[j])==target:
                        arr[0] = min(i,j)
                        arr[1] = max(i,j)
        return arr
       