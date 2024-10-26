# FAIL: TIME OVER
# DFS approach

import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

def retrieve(i, j):
    routes = 0
    num = arr[i][j]
    if num == 0:

        return 1
    if j + num < N:
        routes += retrieve(i, j + num)
    if i + num < N:
        routes += retrieve(i + num, j)
    return routes

print(retrieve(0, 0))

# SOLVE
# DP approach
import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]

dp[0][0] = 1

for i in range(N):
    for j in range(N):
        num = arr[i][j]
        if i == N - 1 and j == N - 1:
            print(dp[-1][-1])
            break
        if dp[i][j] == 0:
            continue
        if j + num < N:
            dp[i][j + num] += dp[i][j]
        if i + num < N:
            dp[i + num][j] += dp[i][j]
