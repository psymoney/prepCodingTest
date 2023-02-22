import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
G = [list(map(int, input().split('\n')[0])) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

Q = deque()
group = []

for i in range(N):
    for j in range(N):
        if G[i][j] == 1 and visited[i][j] == 0:
            traversed = 0
            Q.append((i, j))
            while Q:
                x, y = Q.popleft()
                if visited[x][y] != 0:
                    continue
                visited[x][y] = 1
                traversed += 1
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if nx < 0 or nx >= N or ny < 0 or ny >= N:
                        continue
                    if G[nx][ny] == 0 or visited[nx][ny] != 0:
                        continue
                    if G[nx][ny] == 1 and visited[nx][ny] == 0:
                        Q.append((nx, ny))
            group.append(traversed)

print(len(group))
for i in sorted(group):
    print(i)