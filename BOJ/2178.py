
global N, M
N, M = map(int, input().split())

global G
G = [list(map(int, input())) for _ in range(N)]

global dx, dy
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def traverse(x, y):
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if G[nx][ny] == 0:
            continue
        if G[nx][ny] == 1 or G[nx][ny] > G[x][y] + 1:
            G[nx][ny] = G[x][y] + 1
            traverse(nx, ny)

traverse(0,0)
print(G[N-1][M-1])
