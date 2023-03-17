import sys
import math
from collections import deque

def get_answer(N):
    Q = deque()
    Q.append([1, 0])
    dp = [math.inf] * (N + 1)
    H = [0] * (N + 1)

    min_depth = 0
    trace = str(N)
    while Q:
        idx, cnt = Q.popleft()
        if idx == N:
            min_depth = cnt
            break

        if idx * 3 <= N and cnt + 1 < dp[idx * 3]:
            Q.append([idx * 3, cnt + 1])
            dp[idx * 3] = cnt + 1
            H[idx * 3] = idx
        if idx * 2 <= N and cnt + 1 < dp[idx * 2]:
            Q.append([idx * 2, cnt + 1])
            dp[idx * 2] = cnt + 1
            H[idx * 2] = idx
        if idx + 1 <= N and cnt + 1 < dp[idx + 1]:
            Q.append([idx + 1, cnt + 1])
            dp[idx + 1] = cnt + 1
            H[idx + 1] = idx
    i = N
    while i > 1:
        trace += f' {H[i]}'
        i = H[i]

    return [min_depth, trace]

def sol():
    input = sys.stdin.readline
    N = int(input())
    answers = get_answer(N)
    print(answers[0])
    print(answers[1])

def test():
    TEST_CASES = [
        [2, 1, "2 1"],
        [10, 3, "10 9 3 1"],
        [642, 10, "642 214 107 106 53 52 26 13 12 4 2 1"]
    ]

    for (i, case) in enumerate(TEST_CASES):
        answers = get_answer(case[0])
        if answers[0] != case[1] and answers[1] != case[2]:
            print(f'test case #{i+1} has been failed!'
                  f'answers[0] is expected to be {case[1]}, but {answers[0]} is given'
                  f'answers[1] is expected to be \n{case[2]}\n, but the given is \n{answers[1]}')

test()
sol()