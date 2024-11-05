class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        for e in num:
            while stack and k > 0 and stack[-1] > e:
                stack.pop()
                k -= 1
            stack.append(e)
        
        stack = stack[:-k] if k else stack
        
        result = ''.join(stack).lstrip('0')
        
        return result if result else '0'