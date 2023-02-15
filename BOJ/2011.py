import sys


def sol():
    input = sys.stdin.readline
    num = input().replace("\n", "")

    sections = []
    for i in range(len(num)):
        if i == 0:
            if num[i] == 0:
                return 0
            sections.append(1)
            continue
        if int(num[i]) == 0:
            sections[-1] -= 1
            continue
        if int(num[i - 1]) == 0:
            sections.append(1)
            continue

        concat_num = int(num[i-1] + num[i])
        if 1 <= concat_num <= 26:
            sections[-1] += 1
        else:
            sections.append(1)

    N = max(sections)

    dp = [0, 1, 2]
    ans = 1
    while len(dp) - 1 < N:
        dp.append((dp[-1] + dp[-2]) % 1000000)

    for s in sections:
        if s == 0:
            continue
        ans *= dp[s]
    return ans

print(sol())