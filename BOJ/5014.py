from collections import deque
import sys

F, S, G, U, D = map(int, sys.stdin.readline().split())

Q = deque()
Q.append((S, 0))
M = [U, -D]
V = [0] * (F + 1)
result = 'use the stairs'
while Q:
    f, cnt = Q.popleft()
    if f == G:
        result = cnt
        break
    for m in M:
        if 1 <= f + m <= F and V[f + m] == 0:
            Q.append((f + m, cnt + 1))
            V[f + m] = 1
print(result)