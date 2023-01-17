import sys

input = sys.stdin.readline


class Node:
  def __init__(self, v):
    self.v = v
    self.visited = False
    self.adjacent = []

  def visit(self):
    print(self.v, end=' ')
    self.visited = True


def dfs(root):
  if root is None:
    return
  root.visit()

  for node in root.adjacent:
    if not node.visited:
      dfs(node)


def bfs(root):
  q = []
  root.visit()
  q.append(root.adjacent[i]) for i in range(len(root.adjacent))
  idx = 0
  
  while len(q) > idx:
    q[idx].visit()
    for node in q[idx].adjacent:
      if not node.visited:
        node.visit()
        q.append(node)
    
    idx += 1


n, m, v = list(map(int, input().split(' ')))

nodes = [Node(i) for i in range(n + 1)]

for i in range(m):
  i, j = list(map(int, input().split(' ')))
  nodes[i].adjacent.append(nodes[j])

search(nodes[v])
