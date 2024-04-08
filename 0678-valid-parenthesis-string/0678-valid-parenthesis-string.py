class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        asterisks = []
        
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == '*':
                asterisks.append(i)
            else:
                if stack:
                    stack.pop()
                elif asterisks:
                    asterisks.pop()
                else:
                    return False
                
        while len(stack) and len(asterisks):
            if stack.pop() > asterisks.pop():
                return False
            
        if len(stack) > 0:
            return False
        return True
