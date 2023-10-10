import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

vips = [0]
sections = []
for _ in range(M):
    vips.append(int(input()))
    sections.append(vips[-1] - vips[-2] - 1)
sections.append(N - vips[-1])

dp = [0, 1, 2]
cases = 1
while len(dp) < max(sections) + 1:
    dp.append(dp[-1] + dp[-2])

for section in sections:
    if section == 0:
        continue
    cases *= dp[section]

print(cases)

