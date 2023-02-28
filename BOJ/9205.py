import sys
input = sys.stdin.readline

def initiate_nodes_and_adjacent(nodes: list, adj: list, n: int) -> None:
    for i in range(n):
        nodes[i] = list(map(int, input().split()))
        nodes[i].append(0)

    for i in range(n - 1):
        for j in range(i + 1, n):
            x1, y1, v = nodes[i]
            x2, y2, v = nodes[j]
            dist = abs(x2 - x1) + (y2 - y1)
            if dist <= 1000:
                adj[i].append(j)
                adj[j].append(i)


def bfs(nodes: list, adj: list, n: int) -> None:
    Q = adj[0]
    nodes[0][2] = 1
    while Q:
        i = Q.pop()
        if i == n - 1:
            return
        for a in adj[i]:
            if nodes[a][2] == 0:
                nodes[a][2] = 1
                Q.append(a)


def test() -> str:
    n = int(input()) + 2
    nodes = [[] for _ in range(n)]
    adj = [[] for _ in range(n)]

    initiate_nodes_and_adjacent(nodes, adj, n)
    bfs(nodes, adj, n)

    return 'happy' if nodes[-1][-1] == 1 else 'sad'


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        print(test())
