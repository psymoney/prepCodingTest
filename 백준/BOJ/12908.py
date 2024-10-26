"""
link: https://www.acmicpc.net/problem/12908
title: 텔레포트 3
tier: gold 3
"""
import sys

# override input method for shorter input delay
input = sys.stdin.readline

# input parameters
start = list(map(int, input().split()))
end = list(map(int, input().split()))
coordinates = [list(map(int, input().split())) for _ in range(3)]

# initiate and set answer with distance(time) from start to end
answer = abs(start[0] - end[0]) + abs(start[1] - end[1])

for coo in coordinates:
    t1 = 10 + abs(start[0] - coo[0]) + abs(start[1] - coo[1]) + abs(coo[2] - end[0]) + abs(coo[3] - end[1])
    t2 = 10 + abs(start[0] - coo[2]) + abs(start[1] - coo[3]) + abs(coo[0] - end[0]) + abs(coo[1] - end[1])
    answer = min([answer, t1, t2])


print(answer)
