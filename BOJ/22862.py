import sys

def solution(N, K, series):
    L, R = 0, 0
    length = 0
    max_length = 0
    K_cnt = 0

    for R in range(N):
        if series[R] % 2 == 1:
            K_cnt += 1
            if K_cnt > K:
                if series[L] % 2 == 1:
                    K_cnt -= 1
                else:
                    length -= 1
            L += 1
        else:
            length += 1
            max_length = max(length, max_length)

    return max_length

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
        [10, 5, list(map(int, "1 1 1 1 1 1 1 1 1 1".split())), 0]
    ]

    for idx, (N, K, series, answer) in enumerate(test_cases):
        result = solution(N, K, series)
        print(f'N = {N}, K = {K}, series = {series}, answer = {answer}, result = {result}')
        if result != answer:
            print(f'case #{idx + 1} is wrong!\nanswer is {answer}, but {result} is given.')
        else:
            print(f'case #{idx + 1} pass!')


if __name__ == '__main__':
    DEBUG = True
    if DEBUG:
        test()
    main()