import sys

def sol():
    input = sys.stdin.readline
    N = int(input())
    dp = [0] * (N + 2)
    M = 0

    for i in range(1, N + 1):
        t, p = map(int, input().split())

        if dp[i] > M:
            M = dp[i]
        if i + t > N+1:
            continue

        dp[i + t] = max(dp[i + t], M + p)

    return max(dp)

print(sol())

def test(tasks):
    N = len(tasks)
    dp = [0] * (N + 2)
    m = 0
    for i, (t, p) in enumerate(tasks):
        i += 1
        if dp[i] > m:
            m = dp[i]
        if i + t > N+1:
            continue
        dp[i + t] = max(dp[i + t], m + p)

    return max(dp)

cases = [
    ([(1, 5), (3, 1), (1, 1)], 6),
    ([(3, 10), (5, 20), (1, 10), (1, 20), (2, 15), (4, 40), (2, 200)], 45),
    ([(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10)], 55),
    ([(5, 10), (5, 9), (5, 8), (5, 7), (5, 6), (5, 10), (5, 9), (5, 8), (5, 7), (5, 6)], 20),
    ([(5, 50), (4, 40), (3, 30), (2, 20), (1, 10), (1, 10), (2, 20), (3, 30), (4, 40), (5, 50)], 90),
]

for i, (tasks, expected) in enumerate(cases):
    result = test(tasks)
    if result != expected:
        print(f'case #{i + 1} is wrong!\n{expected} is expected, but {result} is given')
