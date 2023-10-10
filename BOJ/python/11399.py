import sys
input = sys.stdin.readline
N = int(input())
P = sorted(list(map(int, input().split())))
total = 0
part_sum = 0
for p in P:
    part_sum += p
    total += part_sum
print(total)