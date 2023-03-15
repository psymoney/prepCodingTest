import sys
from collections import deque
input = sys.stdin.readline

N, C = map(int, input().split())
M = int(input())
orders = [[] for _ in range(N)]

for _ in range(M):
    s, e, c = map(int, input().split())
    orders[s].append([s, e, c])

for i in range(1, N):
    orders[i].sort(key=lambda x: x[1])

total_amount = 0
amount = 0
carry = deque()
for order in orders:
    if amount == C:
        break
    if len(order) == 0:
        continue

    for s, e, c in order:
        left_space = C - amount
        if left_space > 0:
            if c > left_space:
                carry.append([s, e, left_space])
                amount += left_space
                total_amount += left_space
            else:
                carry.append([s, e, c])
                amount += c
                total_amount += c
        if amount == C:
            break

while len(carry) > 0:
    s, e, c = carry.popleft()
    amount -= c
    left_space = C - amount
    for i in range(e, N):
        if len(orders[i]) == 0:
            continue
        for order in orders[i]:
            s2, e2, c2 = order

            if c2 >= left_space:
                carry.append([s2, e2, left_space])
                order[2] -= left_space
                amount += left_space
                total_amount += left_space
                left_space = 0
                break
            if c2 < left_space:
                carry.append([s2, e2, c2])
                order[2] = 0
                amount += c2
                total_amount += c2
                left_space -= c2

        if left_space == 0:
            break

print(total_amount)