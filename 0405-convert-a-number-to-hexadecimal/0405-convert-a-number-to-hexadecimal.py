class Solution:
    def toHex(self, num: int) -> str:
        hex_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
        
        if num >= 0:
            s = ['' for _ in range(8)]
            
            for i in range(7, -1, -1):
                rem = num % 16
                num = num // 16
                s[i] = hex_chars[rem]
                if num == 0: break
                    
            return ''.join(s)
        
        else:
            num *= -1
            s = ['f' for _ in range(8)]
            prev = False
            
            for i in range(7, -1, -1):
                rem = num % 16
                rem += 1 if prev else 0
                num = num // 16
                s[i] = hex_chars[-rem]
                prev = True if rem else False
                if num == 0: break
                    
            return ''.join(s)
            
        