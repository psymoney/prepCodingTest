import sys

def answer(N: list) -> int:
    l, r = 0, len(N) - 1
    dist = 0

    while l != r:
        dl, dr = sum(N[l:r]), sum(N[r:]) + sum(N[:l])
        dist = max(dist, min(dl, dr))
        if dl > dr:
            l += 1
        else:
            r -= 1

    return dist


def sol() -> None:
    input = sys.stdin.readline
    n = int(input())
    N = [int(input()) for _ in range(n)]
    print(answer(N))

def test() -> None:
    cases = [
        [[1, 2, 3, 4, 5], 7],
        [[6, 9, 7, 4, 2], 13]
    ]

    for i, (N, expected) in enumerate(cases):
        result = answer(N)
        if result != expected:
            print(f'case #{i + 1} is wrong!\n{expected} is expected, but {result} is given')

test()