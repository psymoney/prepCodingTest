import sys
input = sys.stdin.readline

N, X = map(int, input().split())
visitors = list(map(int, input().split()))
max_visitor = 0
cur_visitor = 0
periods = 0

for i in range(len(visitors)):
    cur_visitor += visitors[i]
    if i >= X:
        cur_visitor -= visitors[i-X]
    if cur_visitor > max_visitor:
        max_visitor = cur_visitor
        periods = 1
    elif cur_visitor == max_visitor:
        periods += 1

if max_visitor == 0:
    print('SAD')
else:
    print(max_visitor)
    print(periods)