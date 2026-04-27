class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        flag=False
        arr={}
        for ch in s1:
            arr[ch]=arr.get(ch,0)+1
        i=0
        j=len(s1)
        while(i<=(len(s2)-len(s1))):
            check_str=s2[i:j]
            arr2={}
            for ch in check_str:
                arr2[ch]=arr2.get(ch,0)+1
            if arr==arr2:
                flag = True
                break
            else:
                j+=1
                i+=1
        return flag


