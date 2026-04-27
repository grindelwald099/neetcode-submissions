class Solution:
    def minWindow(self, s: str, t: str) -> str:
        flag=False
        arr=[]
        val=[]
        if s==t:
            return s
        arr=Counter(t)
        i=0
        j=len(t)
        while(j<=len(s)):
            arr2=[]
            newstr=(s[i:j])
            arr2=Counter(newstr)
            if arr <= arr2:
                val.append(s[i:j])
                i+=1
            else:
                j+=1
        val=sorted(val,key=len,reverse=False)
        if len(val)==0:
            return ""
        return val[0]

        