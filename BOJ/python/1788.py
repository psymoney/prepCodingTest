import sys
input = sys.stdin.readline

n = int(input())
m = 1000000000
ARR = [0, 1]

for i in range(2, abs(n)+1):
    ARR.append((ARR[i-1] + ARR[i-2]) % m)

if n < 0 and n % 2 == 0:
    print(-1)
elif n == 0:
    print(0)
else:
    print(1)
print(ARR[abs(n)])
