def solve(init: int):
    cnt = 0
    _next = init
    
    while True:
        cnt += 1
        _next = _next % 10 * 10 + (_next // 10 + _next % 10) % 10;
        
        if _next == init:
            return cnt
            
n = int(input())
print(solve(n))