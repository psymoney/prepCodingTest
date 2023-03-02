import sys
input = sys.stdin.readline

N, M = map(int, input().split())
r, c, v = map(int, input().split())
D = [(0, -1), (1, 0), (0, 1), (-1, 0)]
G = []
for _ in range(N):
    G.append(list(map(int, input().split())))

Q = [(r, c, v)]
times = 0
while Q:
    y, x, d = Q.pop()
    if G[y][x] == 0:
        G[y][x] = -1    # clean this tile
        times += 1

    is_dirty = False

    for dx, dy in D:
        nx = x + dx
        ny = y + dy
        if G[ny][nx] == 0:
            is_dirty = True
            break

    if is_dirty:
        for _ in range(4):
            d = (d + 3) % 4
            dx, dy = D[d]
            nx = x + dx
            ny = y + dy
            if G[ny][nx] == 0:
                Q.append((ny, nx, d))
                break

    else:
        dx, dy = D[(d + 2) % 4]
        nx = x + dx
        ny = y + dy
        if G[ny][nx] != 1:
            Q.append((ny, nx, d))

print(times)
