# first submit
"""
without consideration of conditions of the problem made this inefficient code, having O(n^2)
please read the question and conditions carefully! 
"""
import math

n, k = map(int, input().split(" "))
denominators = [int(input()) for _ in range(n)]
coins = 0

while k != 0:
  min = math.inf
  c = 0
  for d in denominators:
    if k < d:
      break
    if k // d < min:
      min = k // d
      c = d
  coins += min
  k = k % c

print(coins)

# second submit
import math

n, k = map(int, input().split(" "))
d = [int(input()) for _ in range(n)]
coins = 0

for i in range(n-1, -1, -1):
  if k == 0:
    break
  if d[i] > k:
    continue
  coins += k // d[i]
  k = k % d[i]

print(coins)
