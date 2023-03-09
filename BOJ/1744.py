import sys
from heapq import heappop, heappush

input = sys.stdin.readline
N = int(input())
PQ = []
MQ = []
max_sum = 0
for _ in range(N):
    n = int(input())
    if n > 0:
        heappush(PQ, -n)
    elif n == 1:
        max_sum += 1
    else:
        heappush(MQ, n)

while len(PQ) > 1:
    a, b = heappop(PQ) * (-1), heappop(PQ) * (-1)
    max_sum += max(a * b, a + b)

while len(MQ) > 1:
    a, b = heappop(MQ), heappop(MQ)
    max_sum += max(a * b, a + b)

for pq in PQ:
    max_sum -= pq
for mq in MQ:
    max_sum += mq

print(max_sum)

