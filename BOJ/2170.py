import sys
input = sys.stdin.readline

N = int(input())
lines = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: x[0])

length = lines[0][1] - lines[0][0]
longest = lines[0][1]

for i in range(1, N):
    prev_line = lines[i - 1]
    curr_line = lines[i]
    if curr_line[0] <= longest < curr_line[1]:
        length += curr_line[1] - longest
        longest = curr_line[1]
    elif curr_line[0] > longest:
        length += curr_line[1] - curr_line[0]
        longest = curr_line[1]

print(length)
