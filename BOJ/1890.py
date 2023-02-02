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
