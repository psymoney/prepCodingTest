import sys

def answer(P):
    N = len(P)
    M = len(P[0])
    max_util = 0

    for i in range(0, M-2):
        for j in range(i+1, M-1):
            for k in range(j+1, M):
                max_util = max(max_util, sum([max([P[n][i], P[n][j], P[n][k]]) for n in range(N)]))

    return max_util

def sol():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    print(answer(P))

sol()


def test():
    cases = [
        ([
            [1, 2, 3, 4, 5],
            [5, 4, 3, 2, 1],
            [1, 2, 3, 2, 1]
        ], 13),
        ([
             [1, 2, 3, 4, 5, 6],
             [6, 5, 4, 3, 2, 1],
             [3, 2, 7, 9, 2, 5],
             [4, 5, 6, 3, 2, 1]
        ], 25),
        ([[1, 2, 3, 4, 5]], 5),
        ([
             [1, 2, 3, 4, 5],
             [1, 2, 3, 4, 5],
             [1, 2, 3, 4, 5],
             [1, 2, 3, 4, 5]
        ], 20)

    ]

    for i, (case, expected) in enumerate(cases):

        result = answer(case)
        if result != expected:
            print(f'case #{i + 1} is wrong!\n{expected} is expected, but {result} is given')

test()