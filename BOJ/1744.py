"""
문제 풀이 접근 방법:
1. 1보다 작은 정수들은 각각의 수를 곱하면 0보다 크거나 같은 정수가 된다. (-N * -2N = 2N^2; -N * 0 = 0 > -N)
2. 1은 어떤 임의의 양수와 곱해도 1과 해당 양수의 합보다 작다. (N < N + 1)
3. 0과 1을 제외한 두개의 임의의 정수의 절댓값의 곱은 임의의 정수가 클수록 결괏값이 커지므로 음의 정수는 오름차순, 양의 정수는 내림차순으로 정렬한다.
4. 최대 입력값 N은 50으로 O(N^2)를 갖는 알고리즘을 채택하여도 크게 문제가 없으나, 양의 정수를 담는 배열과 음의 정수를 담는 배열 두 개를 우선순위 큐로 구성하여 문제 해결하였음.
"""

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

