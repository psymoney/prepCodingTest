import sys
input = sys.stdin.readline

N = int(input())
classes = sorted([tuple(map(int, input().split())) for _ in range(N)], key=lambda x: x[0])
classrooms = [classes[0][1]]
earliest = classrooms[0]

for i in range(1, N):
    if classes[i][0] < earliest:
        classrooms.append(classes[i][1])
    else:
        classrooms[classrooms.index(earliest)] = classes[i][1]
    earliest = min(classrooms)

print(len(classrooms))
