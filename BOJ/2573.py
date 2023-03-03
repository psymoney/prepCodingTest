import sys
input = sys.stdin.readline

N, M = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(N)]
D = [(0, -1), (-1, 0), (0, 1), (1, 0)]
Q = []

# second approach: decrease glacial while traversing graph, and then check the glacial is separated
year = 0
while True:
    # check the glacial is scattered
    V = [[True] * M] + [([True] + [0] * (M - 2) + [True]) for _ in range(N - 2)] + [[True] * M]
    bunches = 0
    for y in range(1, N - 1):
        for x in range(1, M - 1):
            if G[y][x] == 0:
                V[y][x] = True
            if G[y][x] != 0 and not V[y][x]:
                V[y][x] = True
                Q = [(x, y)]
                bunches += 1
                if bunches >= 2:
                    print(year)
                    quit()
                while Q:
                    x2, y2 = Q.pop()
                    for dx, dy in D:
                        nx, ny = x2 + dx, y2 + dy
                        if 0 <= nx < M and 0 <= ny < N and not V[ny][nx] and G[ny][nx] > 0:
                            Q.append((nx, ny))
                            V[ny][nx] = True
    if bunches == 0:
        print(0)
        quit()

    # traverse graph and melt the glacial
    for y in range(1, N - 1):
        for x in range(1, M - 1):
            if G[y][x] == 0:
                continue
            num_seas = 0
            for dx, dy in D:
                nx, ny = x + dx, y + dy
                if 0 <= nx < M and 0 <= ny < N and G[ny][nx] == 0:
                    num_seas += 1
            G[y][x] = G[y][x] - num_seas if num_seas <= G[y][x] else 0
    year += 1







