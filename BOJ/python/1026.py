import sys
IN = sys.stdin.readline

N = int(IN())
A = sorted(list(map(int, IN().split())))
B = sorted(list(map(int, IN().split())), reverse=True)
total = 0
for i in range(N):
    total += A[i] * B[i]
print(total)