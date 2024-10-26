import sys
input = sys.stdin.readline
N, K = map(int, input().split())
C = sorted([int(input()) for _ in range(N)])
T = C[0]
n = 0
for i in range(1, N):
    n = i
    gap = C[i] - C[i-1]
    if K >= gap * i:
        T += gap
        K -= gap * i
    else:
        T += K // i
        K -= (K // i) * i
        break

T += K // (n+1)
print(T)


