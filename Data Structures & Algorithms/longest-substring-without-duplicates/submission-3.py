class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        arr=[]
        if s=="":
            return 0
        if (len(s)==1):
            return 1
        for i in range(len(s)-1):
            b=""
            b+=s[i]
            for j in range(i+1,len(s)):
                b+=s[j]
                if len(b)!=len(set(b)):
                    arr.append(len(set(b)))
                    break
                else:
                    arr.append(len(b))
        arr=sorted(arr,reverse=True)
        return arr[0]
            
