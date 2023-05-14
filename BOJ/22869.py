import sys

def answer(N: int, K: int, stones: list) -> str:
    dp = [True] + [False] * (N - 1)

    for i in range(0, N-1):
        if not dp[i]:
            continue

        for j in range(i+1, N):
            force = (j - i) * (1 + abs(stones[i] - stones[j]))
            if force <= K:
                dp[j] = True

    return 'YES' if dp[N-1] else 'NO'


def sol() -> None:
    input = sys.stdin.readline
    N, K = map(int, input().split())
    stones = list(map(int, input().split()))
    print(answer(N, K, stones))

def test() -> None:
    cases = [
        [(5, 3, [1, 4, 1, 3, 1]), 'YES'],
        [(5, 3, [1, 5, 2, 1, 6]), 'NO']
    ]

    for case in cases:
        result = answer(*case[0])
        if result != case[1]:
            print(f'Wrong answer: {result}, expected: {case[1]}')


test()

