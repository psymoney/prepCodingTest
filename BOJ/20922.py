import sys
input = sys.stdin.readline
N, K = map(int, input().split())
records = [0] * (100001)
numbers = list(map(int, input().split()))
max_partial_length = 0
cur_partial_length = 0
for number in numbers:
    if records[number] == K:
        max_partial_length = max(max_partial_length, cur_partial_length)
        cur_partial_length = 1
        records = [0] * (100001)
    records[number] += 1
    cur_partial_length += 1
print(max_partial_length)