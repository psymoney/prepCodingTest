import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
L = sorted(A + B)
result = ''
for i in range(N + M):
    if i == N + M - 1:
        result += str(L[i])
    else:
        result += str(L[i]) + ' '
print(result)