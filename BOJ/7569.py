import sys

input = sys.stdin.readline
M, N, H = map(int, input().split())
G = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

def traverse(points, G, day):
    Q = [points]
    D = [(0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1), (1, 0, 0), (-1, 0, 0)]
    while Q:
        h, n, m = Q.pop()
        for dh, dn, dm in D:
            nh = h + dh
            nn = n + dn
            nm = m + dm
            if 0 <= nh < H and 0 <= nn < N and 0 <= nm < M:
                if G[nh][nn][nm] == day:
                    Q.append((nh, nn, nm))
                    G[nh][nn][nm] = -1  # change riped tomato's status
                if G[nh][nn][nm] == 0:
                    G[nh][nn][nm] = day + 1  # change next tomato's status

def iterate(G, day):
    cnt = 0
    for h in range(len(G)):
        for n in range(len(G[0])):
            for m in range(len(G[0][0])):
                if G[h][n][m] == day:
                    cnt += 1
                    traverse((h, n, m), G, day)
    return cnt

day = -1

while True:
    cnt = iterate(G, day + 2)
    if cnt == 0:
        break
    day += 1

for h in range(H):
    for n in range(N):
        for m in range(M):
            if G[h][n][m] == 0:
                day = -1

print(day)
