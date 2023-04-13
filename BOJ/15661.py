import sys
from itertools import combinations
from math import inf

def answer(S):
    N = len(S)
    M = inf

    for n in range(1, N): # O(N) max(N) = 20
        cases = combinations(range(N), n) # O(N^2)
        for case in cases:
            a, b = 0, 0
            for i in range(N):
                i += 1
                in_i = i in case
                for j in range(N):
                    j += 1
                    if i == j:
                        continue
                    in_j = j in case
                    if in_i and in_j:
                        a += S[i-1][j-1]
                    elif not in_i and not in_j:
                        b += S[i-1][j-1]
            M = min(M, abs(a-b))

    return M

def sol():
    input = sys.stdin.readline
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]
    print(answer(S))


def test():
    cases = [
        ([
            [0, 1, 2, 3],
            [4, 0, 5, 6],
            [7, 1, 0, 2],
            [3, 4, 5, 0]
        ], 0),
        ([
            [0, 1, 2, 3, 4, 5],
            [1, 0, 2, 3, 4, 5],
            [1, 2, 0, 3, 4, 5],
            [1, 2, 3, 0, 4, 5],
            [1, 2, 3, 4, 0, 5],
            [1, 2, 3, 4, 5, 0]
        ], 2),
        ([
            [0, 5, 4, 5, 4, 5, 4, 5],
            [4, 0, 5, 1, 2, 3, 4, 5],
            [9, 8, 0, 1, 2, 3, 1, 2],
            [9, 9, 9, 0, 9, 9, 9, 9],
            [1, 1, 1, 1, 0, 1, 1, 1],
            [8, 7, 6, 5, 4, 0, 3, 2],
            [9, 1, 9, 1, 9, 1, 0, 9],
            [6, 5, 4, 3, 2, 1, 9, 0]
        ], 1),
        ([
            [0, 3, 1, 1, 1],
            [3, 0, 1, 1, 1],
            [1, 1, 0, 1, 1],
            [1, 1, 1, 0, 1],
            [1, 1, 1, 1, 0]
        ], 0)
    ]

    for i, (case, expected) in enumerate(cases):
        result = answer(case)
        if result != expected:
            print(f'case #{i + 1} is wrong!\n{expected} is expected, but {result} is given')

test()