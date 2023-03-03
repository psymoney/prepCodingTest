import sys
input = sys.stdin.readline

N, M = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(N)]
V = [[True] * M] + [([True] + [0] * (M - 2) + [True]) for _ in range(N)] + [[True] * M]
D = [(0, -1), (-1, 0), (0, 1), (1, 0)]
Q = []
print(V)

# first approach: check everything while traverse
year = 0
while True:
    continents = 0
    for y in range(1, N - 1):
        for x in range(1, M - 1):
            # need to check the case all 0
            if V[y][x]:
                continue
            V[y][x] = True
            if G[y][x] != 0:
                continents += 1
                if continents >= 2:
                    print(year)
                    quit()
                # count adjacent
                Q = []
                adj = 0
                for dx, dy in D:
                    nx, ny = x + dx, y + dy
                    if G[ny][nx] == 0:
                        adj += 1
                        continue
                    if G[ny][nx] != 0 and not V[ny][nx]:
                        V[ny][nx] = True
                        Q.append((nx, ny))
                G[y][x] -= adj if adj <= G[y][x] else 0
                while Q:

                pass
        pass

# second approach: decrease glacial while traversing graph, and then check the glacial is separated
year = 0
while True:
    # traverse graph and melt the glacial
    # time pass by 1 year
    while Q:
        x, y = Q.pop()
        if G[y][x] != 0:
            # count adjacent 0
            pass
    year += 1

    # check the glacial is scattered
    # if yes then print -> year then finish the process





