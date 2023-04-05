import sys
from math import inf

def answer(n):
    dp = [0] + [inf] * (n)

    for i in range(n+1):
        for j in range(1, int(n ** 0.5) + 1):
            if i + j ** 2 > n:
                break
            dp[i + j ** 2] = min(dp[i + j ** 2], dp[i] + 1)

    return dp[n]


def sol():
    input = sys.stdin.readline
    N = int(input())
    print(answer(N))

sol()

def test():
    cases = [
        (25, 1),
        (26, 2),
        (11339, 3),
        (34567, 4),
        (100, 1),
        (25987, 3)
    ]

    for i, (case, expected) in enumerate(cases):
        result = answer(case)
        if result != expected:
            print(f'case #{i + 1} is wrong!\n{expected} is expected, but {result} is given')

test()