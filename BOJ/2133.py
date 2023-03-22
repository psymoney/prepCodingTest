def get_answer(N):
    dp = [0, 0, 3]
    if N < 3:
        return dp[N]

    for i in range(3, N + 1):
        if i % 2 == 1:
            dp.append(0)
        if i % 2 == 0:
            dp.append(
                dp[i-2] * 3 + sum(dp[:i-2]) * 2 + 2
            )
    return dp[N]

def sol():
    N = int(input())
    print(get_answer(N))

def test():
    test_cases = [(1, 0), (2, 3), (3, 0), (4, 11), (5, 0), (6, 41), (7, 0), (8, 153), (10, 571), (30, 299303201)]
    for i, (n, answer) in enumerate(test_cases):
        result = get_answer(n)
        if result != answer:
            print(f'case #{i + 1} is wrong!\nanswer is {answer} but {result} given')

test()