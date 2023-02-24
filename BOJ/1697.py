from collections import deque

N, K = map(int, input().split())
M = 100000
def bfs(N, K):
    Q = deque()
    Q.append(N)
    visited = [0] * (M+1)
    visited[N] = 1
    while Q:
        n = Q.popleft()
        if n == K:
            return visited[n]
        for dn in [-1, 1, n]:
            nn = n + dn
            if 0 <= nn <= M and visited[nn] == 0:
                visited[nn] = visited[n] + 1
                Q.append(nn)

print(bfs(N,K) - 1)