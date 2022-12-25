n = int(input())

dp = [[1] * 10]

while len(dp) < n:
    line = []
    for i in range(10):
        line.append(sum(dp[-1][:i+1]))
    dp.append(line)

print(sum(dp[n-1])%10007)
