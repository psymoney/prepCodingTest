class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        r = 0
        
        for i in range(len(s)):
            c = s[i]
            if c == '(':
                stack.append(c)
            elif c == ')':
                if len(stack) == 0:
                    continue
                r = max(len(stack), r)
                stack.pop()
            elif c in ['+', '-', '*', '/']:
                continue
            
        
        return r if len(stack) == 0 else 0
                
        