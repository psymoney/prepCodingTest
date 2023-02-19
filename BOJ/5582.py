import sys
input = sys.stdin.readline

str_1 = input().replace("\n", "")
str_2 = input().replace("\n", "")

dp = [[0] * (len(str_2) + 1) for _ in range(len(str_1) + 1)]
max = 0
for i in range(len(str_1)):
    for j in range(len(str_2)):
        if str_1[i] == str_2[j]:
            v = dp[i][j] + 1
            max = v if v > max else max
            dp[i+1][j+1] = v

print(max)
