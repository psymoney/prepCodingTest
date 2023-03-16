import sys
from collections import deque
input = sys.stdin.readline
N, K = map(int, input().split())
records = [deque([]) for _ in range(100001)]
numbers = list(map(int, input().split()))
max_partial_length = 0
cur_partial_length = 0
cur_char_index = 0
for idx in range(N):
    num = numbers[idx]
    if len(records[num]) == K:
        last_idx = records[num].popleft()
        if last_idx < cur_char_index:
            pass
        else:
            max_partial_length = max(max_partial_length, cur_partial_length)
            cur_partial_length = idx - last_idx - 1
            cur_char_index = last_idx + 1
    records[num].append(idx)
    cur_partial_length += 1
max_partial_length = max(max_partial_length, cur_partial_length)
print(max_partial_length)