class Solution:
    def isAnagram(self, s: str, t: str) -> bool: 
        arr={}
        arr2={}
        if(len(s) != len(t)):
            return False
        for ch in s:
            cnt=0
            arr[ch] = arr.get(ch, 0) + 1
        for ch2 in t:
            if ch2 not in arr:
                return False
                break
            else:
                arr2[ch2] = arr2.get(ch2, 0) + 1
        if arr == arr2:
            return True
        else:
            return False
            
        
            


            

