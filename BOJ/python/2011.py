import sys
input = sys.stdin.readline
n = input().replace('\n', "")
l = len(n)
dp = [0] * (l + 1)
if int(n[0]) == 0:
    print(0)
else:
    dp[0], dp[1] = 1, 1
    n = "0" + n

    for i in range(2, l + 1):
        num = int(n[i-1] + n[i])
        if int(n[i]) > 0:
            dp[i] += dp[i-1]
        if 10 <= num <= 26:
            dp[i] += dp[i-2]
    print(dp[l] % 1000000)