import sys

input = sys.stdin.readline

dfs_values = []
bfs_values = []

class Node:
    def __init__(self, v):
        self.v = v
        self.visited = False
        self.adjacent = []

    def visit(self):
        self.visited = True


# different result compared with example
def dfs(root):
    if root is None:
        return
    root.visit()
    dfs_values.append(root.v)

    for node in root.adjacent:
        if not node.visited:
            dfs(node)

# not even traverse all adjacent
def bfs(root):
    q = []
    root.visit()
    bfs_values.append(root.v)
    for i in root.adjacent:
        q.append(i) 
    idx = 0
  
    while len(q) > idx:
        bfs_values.append(q[idx].v)
        for node in q[idx].adjacent:
            if not node.visited:
                node.visited = True
                q.append(node)
    
        idx += 1


n, m, v = list(map(int, input().split(' ')))

nodes = [Node(i) for i in range(n + 1)]


for i in range(m):
    i, j = list(map(int, input().split(' ')))
    nodes[i].adjacent.append(nodes[j])
    # one way adjacent

dfs(nodes[v])
bfs(nodes[v])

result = str(dfs_values[0])
for i in dfs_values[1:]:
    result += ' ' + str(i)
print(result)

result = str(bfs_values[0])
for i in bfs_values[1:]:
    result += ' ' + str(i)
print(result)
