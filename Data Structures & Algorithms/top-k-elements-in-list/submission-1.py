class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        val = {}
        str = []
        for i in range(len(nums)):
            cnt=0
            if(nums[i] in str):
                continue
            for j in range(len(nums)):
                if nums[i]==nums[j]:
                    cnt+=1
            val[nums[i]] = cnt
            str.append(nums[i])
        ans = sorted(val, key=val.get, reverse=True)
        return(ans[:k])

                

        