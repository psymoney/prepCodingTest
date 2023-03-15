N = int(input())
tags_in_line = [0] + list(map(int, input().split()))
tags_in_position = [0] * (N + 1)

for i in range(1, N + 1):
    tags_in_position[tags_in_line[i]] = i

aligned_children = 1
maximum_aligned = 1

for i in range(1, N):
    if tags_in_position[i] < tags_in_position[i+1]:
        aligned_children += 1
    else:
        if aligned_children > maximum_aligned:
            maximum_aligned = aligned_children
        aligned_children = 1

print(N - maximum_aligned)
