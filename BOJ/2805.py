import sys


def answer(T: list, M: int) -> int:
    l, r = 1, max(T)

    while l <= r:
        m = l + (r - l) // 2

        woods = 0
        for t in T:
            if t > m:
                woods += t - m

        if woods < M:
            r = m - 1
        else:
            l = m + 1

    return r

def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    T = list(map(int, input().split()))
    print(answer(T, M))

# solve()

def test():
    CASES = [
        [[20, 15, 10, 17], 7, 15],
        [[4, 42, 40, 26, 46], 20, 36],
        [[3, 9], 10, 1]
    ]

    for i, (T, M, expected) in enumerate(CASES):
        result = answer(T, M)
        if result != expected:
            print(f'case #{i + 1} is wrong!\n{expected} is expected, but {result} is given')

test()