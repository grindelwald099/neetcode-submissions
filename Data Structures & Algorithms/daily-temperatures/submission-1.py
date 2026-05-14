class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result=[]
        for i in range(len(temperatures)):
            cnt=1
            if i==(len(temperatures)-1):
                result.append(0)
                break
            for j in range(i+1,len(temperatures)):
                if (j==(len(temperatures)-1)) and (temperatures[i]>=temperatures[j]):
                    result.append(0)
                    break
                if temperatures[j]>temperatures[i]:
                    result.append(cnt)
                    break
                else:
                    cnt+=1
        return result

