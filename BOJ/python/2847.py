import sys
input = sys.stdin.readline
N = int(input())
scores = [int(input()) for _ in range(N)]
last_score = scores[N - 1]
adjust_scores = 0
for i in range(N - 2, -1, -1):
    if last_score <= scores[i]:
        change = scores[i] - last_score + 1
        scores[i] -= change
        adjust_scores += change
    last_score = scores[i]
print(adjust_scores)