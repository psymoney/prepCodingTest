import sys
input = sys.stdin.readline
S = input().rstrip()
prev = S[0]
sections = 1
for i in range(1, len(S)):
    curr = S[i]
    if curr != prev:
        sections += 1
    prev = curr
print(sections // 2)