class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        val=[]
        if len(prices)==1:
            return 0
        for i in range(len(prices)-1):
            max=[]
            for j in range(i+1,len(prices)):
                max.append(prices[j]-prices[i])
            max=sorted(max,reverse=True)
            if max[0]<0:
                val.append(0)
            else:
                val.append(max[0])
        val=sorted(val,reverse=True)
        return val[0]


                
        