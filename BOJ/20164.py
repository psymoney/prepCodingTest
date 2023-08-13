import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
Q = deque([(0, N)])
results = []

while len(Q) > 0: # O(2log N)
    v, n = deque.popleft(Q)
    sn = str(n)
    l = len(str(n))

    sum = 0

    for a in sn:
        sum += 1 if int(a) % 2 != 0 else 0
    if l == 1:
        results.append(sum + v)

    elif l == 2:
        Q.append((v + sum, n // 10 + n % 10))

    elif l >= 3:
        for i in range(1, l - 1):
            for j in range(i + 1, l):
                Q.append((v + sum, int(sn[:i]) + int(sn[i:j]) + int(sn[j:])))

results.sort()  # O(log N)
print(f'{results[0]} {results[-1]}')


