import sys

input = sys.stdin.readline
N = int(input())
boxes = list(map(int, input().split()))

dp = [1]

for i in range(1, N):
    tem = []
    for j in range(i):
        if boxes[i] > boxes[j]:
            tem.append(dp[j] + 1)
    if not tem:
        dp.append(1)
    else:
        dp.append(max(tem))
print(max(dp))
