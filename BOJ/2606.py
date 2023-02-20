import sys
input = sys.stdin.readline

N = int(input())
G = {}
for i in range(1, N + 1):
    G.setdefault(i, [])
n = int(input())
for _ in range(n):
    i, v = map(int, input().split())
    G[i].append(v)

def traverse(idx, group):
    group.append(idx)
    for node in G[idx]:
        if node not in group:
            group = traverse(node, group)

    return group

route = traverse(1, [])
print(len(route) - 1)
