import sys
from collections import deque
input = sys.stdin.readline


def bfs(home: list, stores: list, festival: list) -> str:
    visited = [0] * len(stores)
    Q = deque()
    Q.append(home)
    result = 'sad'
    while Q:
        x1, y1 = Q.popleft()
        if abs(x1 - festival[0]) + abs(y1 - festival[1]) <= 1000:
            return 'happy'
        for i in range(len(stores)):
            x2, y2 = stores[i]
            dist = abs(x2 - x1) + abs(y2 - y1)
            if dist <= 1000 and visited[i] == 0:
                Q.append(stores[i])
                visited[i] = 1
    return result


def test() -> str:
    n = int(input())
    home = list(map(int, input().split()))
    stores = [list(map(int, input().split())) for _ in range(n)]
    festival = list(map(int, input().split()))
    print(bfs(home, stores, festival))


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        test()