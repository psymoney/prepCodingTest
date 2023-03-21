import sys

def solution(N, K, series):
    L = 0
    length = 0
    cnt = 0

    for R in range(N):
        while L < R and series[L] % 2 == 1:
            L += 1
            cnt -= 1
        if series[R] % 2 == 1:
            cnt += 1
        if cnt > K:
            length = max(length, R - L - cnt + 1)
        if R == N - 1:
            length = max(length, R - L - cnt + 1)
        while cnt > K and L < R:
            if series[L] % 2 == 1:
                cnt -= 1
            L += 1

    return length

def main():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    series = list(map(int, input().split()))
    print(solution(N, K, series))


def test():
    test_cases = [
        [8, 2, list(map(int, "1 2 3 4 5 6 7 8".split())), 3],
        [5, 1, list(map(int, "2 1 2 1 1".split())), 2],
        [1, 1, [2], 1],
        [10, 1, list(map(int, "1 1 1 1 1 1 1 1 1 1".split())), 0],
        [10, 5, list(map(int, "1 1 1 1 1 1 1 1 1 1".split())), 0],
        [7, 3, list(map(int, "1 2 3 3 3 4 5".split())), 2],
        [12, 3, list(map(int, "1 2 3 3 3 4 5 6 7 8 9 10".split())), 4],
        [14, 3, list(map(int, "3 3 3 3 3 3 3 4 5 6 7 8 9 10".split())), 4]
    ]

    for idx, (N, K, series, answer) in enumerate(test_cases):
        result = solution(N, K, series)
        if result != answer:
            print(f'case #{idx + 1} is wrong!\nanswer is {answer}, but {result} is given.')


if __name__ == '__main__':
    DEBUG = True
    if DEBUG:
        test()
    main()