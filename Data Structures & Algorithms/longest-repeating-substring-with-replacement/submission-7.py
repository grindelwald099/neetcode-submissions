class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i=0
        j=1
        cnt=[]
        while(j<=len(s)):
            temp=s[i:j]
            count = Counter(temp)
            a = count.most_common(1)[0][1]
            if (len(temp)-a)<=k:
                j+=1
                cnt.append(len(temp))
            else:
                i+=1
        cnt=sorted(cnt,reverse=True)
        return cnt[0] 
        