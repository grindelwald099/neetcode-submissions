class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        arr=[]
        arr3=[]
        for i in range(0,len(strs)):
            val_2 = {}
            if (strs[i] in arr3):
                continue
            for ch in strs[i]:
                val_2[ch] = val_2.get(ch,0) + 1
            arr2=[]
            for j in range(0,len(strs)):
                val_1 = {}
                if i==j:
                    continue
                else:
                    for ch in strs[j]:
                        val_1[ch] = val_1.get(ch,0) + 1
                
                if val_1 == val_2:
                    arr2.append(strs[j])
                    arr3.append(strs[j])
            arr.append([strs[i]]+arr2)
        return arr
                    


                    

        