import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    l = []
    l.append(sys.stdin.readline().split())
    l.append(sys.stdin.readline().split())
    dp = [[0, 0]]
    for i in range(1, n + 1):
        dp.append([
            max(dp[i-1][1], dp[i-2][1]) + int(l[0][i-1]),
            max(dp[i-1][0], dp[i-2][0]) + int(l[1][i-1])
        ])    
    print(max(dp[-1]))
  
