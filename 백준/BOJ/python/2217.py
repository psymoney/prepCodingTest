import sys
input = sys.stdin.readline
N = int(input())
ropes = [int(input()) for _ in range(N)]
max_w = 0
for (i, w) in enumerate(sorted(ropes, reverse=True)):
    max_w = max(max_w, w * (i + 1))
print(max_w)