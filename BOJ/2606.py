import sys
input = sys.stdin.readline

N = int(input())
V = int(input())
G = [[] for _ in range(N + 1)]
for _ in range(V):
    i, v = map(int, input().split())
    G[i].append(v)
    G[v].append(i)

def traverse(idx, group):
    group.append(idx)
    for node in G[idx]:
        if node not in group:
            group = traverse(node, group)

    return group

route = traverse(1, [])
print(len(route) - 1)
