import sys
from heapq import *
input = sys.stdin.readline

N = int(input())
classes = sorted([tuple(map(int, input().split())) for _ in range(N)], key=lambda x: x[0])
classrooms = []
heapify(classrooms)
earliest = classes[0][1]

for s, t in classes[1:]:
    if s < earliest:
        if t <= earliest:
            heappush(classrooms, earliest)
            earliest = t
        else:
            heappush(classrooms, t)
    else:
        heappush(classrooms, t)
        earliest = heappop(classrooms)

print(len(classrooms) + 1)
