class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        arr=[]
        i=1
        piles.sort()
        j=max(piles)
        while i<=j:
            k=(i+j)//2
            sum=0
            for a in range(0,len(piles)):
                sum+=math.ceil(piles[a]/k)
            if sum <= h:
                arr.append(k)
                j=k-1
            else:
                i=k+1
        arr.sort()
        return arr[0]
            