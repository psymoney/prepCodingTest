import sys
from heapq import *
input = sys.stdin.readline

N = int(input())
classes = sorted([tuple(map(int, input().split())) for _ in range(N)], key=lambda x: x[0])
classrooms = [classes[0][1]]
heapify(classrooms)

for s, t in classes[1:]:
    if s < classrooms[0]:
        heappush(classrooms, t)
    else:
        heapreplace(classrooms, t)

print(len(classrooms))
