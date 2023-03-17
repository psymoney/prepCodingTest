import sys

def get_answer(N):
    dp = [0] * (N + 1)

    for i in range(1, N+1):
        if i != 1:
            dp[i] = min(dp[i], dp[i-1] + 1) if dp[i] != 0 else dp[i-1] + 1
        if i * 3 <= N:
            dp[i*3] = min(dp[i*3], dp[i] + 1) if dp[i*3] != 0 else dp[i] + 1
        if i * 2 <= N:
            dp[i*2] = min(dp[i*2], dp[i] + 1) if dp[i*2] != 0 else dp[i] + 1

    answer = str(dp[-1]) + "\n" + str(N)
    target = dp[-1] - 1

    for i in range(N-1, 0, -1):
        if dp[i] == target:
            answer += f' {i}'
            target -= 1

    return answer


def sol():
    input = sys.stdin.readline
    N = int(input())
    print(get_answer(N))

def test():
    TEST_CASES = [
        [2, 1, "2 1"],
        [10, 3, "10 9 3 1"]
    ]

    for (i, case) in enumerate(TEST_CASES):
        answer = get_answer(case[0])
        if answer != case[1]:
            print(f'test case #{i+1} has been failed! {case[1]} is expected, but {answer} is given')

sol()