import sys

input = sys.stdin.readline

dfs_str = ''
bfs_str = ''

class Node:
  def __init__(self, v):
    self.v = v
    self.visited = False
    self.adjacent = []

  def visit(self):
    self.visited = True


def dfs(root):
  if root is None:
    return
  root.visit()
  dfs_str += root.v + ' '

  for node in root.adjacent:
    if not node.visited:
      dfs(node)


def bfs(root):
  q = []
  root.visit()
  bfs_str += root.v + ' '
  for i in root.adjacent:
    q.append(i) 
  idx = 0
  
  while len(q) > idx:
    bfs_str += q[idx].v + ' '
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

dfs(nodes[v])
bfs(nodes[v])

print(dfs_str)
print(bfs_str)
