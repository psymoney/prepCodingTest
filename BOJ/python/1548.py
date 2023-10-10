import sys


def answer(N: list) -> int:
    l = len(N)
    if l < 3:
        return l

    M = 2

    for x in range(l - 2):
        for z in range(l - 1, x + 1, -1):
            if N[x] + N[x+1] > N[z]:
                M = max(M, z - x + 1)

    return M

def sol():
    input = sys.stdin.readline
    N = int(input())
    S = sorted(list(map(int, input().split())))
    print(answer(sorted(S)))


def test():
    cases = [
        ([1, 2, 3], 2),
        ([2, 3, 4, 1, 3, 4, 5], 5),
        ([1, 1, 1, 1, 1, 1, 1, 1], 8),
        ([1, 1, 1, 1000000000, 1000000000, 1000000000], 4),
        ([1000000000], 1)
    ]

    for i, (N, expected) in enumerate(cases):
        result = answer(sorted(N))
        if result != expected:
            print(f'case #{i + 1} is wrong!\n{expected} is expected, but {result} is given')

test()