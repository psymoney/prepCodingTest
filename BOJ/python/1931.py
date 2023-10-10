import sys
input = sys.stdin.readline

N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]

meetings.sort(key=lambda x: (x[1], x[0]))
assigned_list = []

for meeting in meetings:
    if len(assigned_list) == 0 or meeting[0] >= assigned_list[-1][1]:
        assigned_list.append(meeting)
print(len(assigned_list))