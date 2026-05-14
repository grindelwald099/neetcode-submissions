class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        val=0
        stack=[]
        for ch in tokens:
            if ch == "+":
                b=stack.pop()
                a=stack.pop()
                stack.append(a+b)
            elif ch == "*":
                b=stack.pop()
                a=stack.pop()
                stack.append(a*b)
            elif ch == "/":
                b=stack.pop()
                a=stack.pop()
                stack.append(int(a/b))
            elif ch == "-":
                b=stack.pop()
                a=stack.pop()
                stack.append(a-b)
            else:
                stack.append(int(ch))
        return stack[0]

        

