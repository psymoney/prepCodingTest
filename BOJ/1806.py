import sys

def answer(L, S):
    partial_sum = [0] * len(L)
    sum = 0

    for i in range(len(L)):
        if L[i] >= S:
            return 1
        sum += L[i]
        partial_sum[i] = sum

    l = 2

    while l < len(L):
        for i in range(len(L) - l):
            if partial_sum[i + l] - partial_sum[i] >= S:
                return l
        l += 1

    return 0


def sol() -> None:
    input = sys.stdin.readline
    N, S = map(int, input().split())
    L = list(map(int, input().split()))
    print(answer(L, S))

sol()

def test() -> None:
    cases = [
        [[5, 1, 3, 5, 10, 7, 4, 9, 2, 8], 15, 2],
    ]

    for i, (L, S, expected) in enumerate(cases):
        result = answer(L, S)
        if result != expected:
            print(f'case #{i + 1} is wrong!\n{expected} is expected, but {result} is given')

test()