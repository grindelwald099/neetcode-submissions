class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        sum=0
        arr=[]
        for i in range(0,(len(numbers)-1)):
            sum=numbers[i]
            for j in range(i+1,(len(numbers))):
                arr.append(i+1)
                arr.append(j+1)
                if (numbers[i]+numbers[j])<target:
                    arr=[]
                    continue
                if (numbers[i]+numbers[j])>target:
                    arr=[]
                    break
                if (numbers[i]+numbers[j])==target:
                    return arr

        