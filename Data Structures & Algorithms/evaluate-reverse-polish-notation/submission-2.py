class Solution:                     
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        ops = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: int(a / b),
}
        for ch in tokens:
            if ch in ops:
                    b=stack.pop()
                    a=stack.pop()
                    stack.append(ops[ch](a,b))
            else:   
                stack.append(int(ch))
        return stack.pop()

                    

