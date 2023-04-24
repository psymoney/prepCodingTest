import sys


def answer(A: list, k: int, c: int) -> int:
    max_kinds = 0
    for i in range(len(A)):
        kinds = set([c])
        for j in range(k):
            kinds.add(A[(i + j) % len(A)])
        max_kinds = max(max_kinds, len(kinds))
    return max_kinds


def sol() -> None:
    input = sys.stdin.readline
    N, d, k, c = map(int, input().split())
    A = [int(input()) for _ in range(N)]
    print(answer(A, k, c))

sol()

def test() -> None:
    cases = [
        [[7, 9, 7, 30, 2, 7, 9, 25], 4, 30, 5],
        [[2, 7, 9, 25, 7, 9, 7, 30], 4, 7, 4]
    ]

    for i, (A, k, c, expected) in enumerate(cases):
        result = answer(A, k, c)
        if result != expected:
            print(f'case #{i + 1} is wrong!\n{expected} is expected, but {result} is given')

test()

