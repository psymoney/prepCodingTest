import sys
input = sys.stdin.readline

N = int(input())
first, second = map(int, input().split())
V = int(input())
G = [[] for _ in range(N + 1)]
for _ in range(V):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

visited = []
chon = [0] * (N + 1)

def traverse(idx):
    visited.append(idx)

    for node in G[idx]:
        if node not in visited:
            chon[node] = chon[idx] + 1
            traverse(node)

traverse(first)
print(chon[second] if chon[second] != 0 else -1)
