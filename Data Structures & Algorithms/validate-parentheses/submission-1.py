class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        check = {')' : "(", "]" : "[", "}" : "{"}
        for ch in s:
            if ch in check:
                if stack and stack[-1] == check[ch]:
                    stack.pop()
                    continue
            stack.append(ch)
        if len(stack)>0:
            return False
        else:
            return True
        


        