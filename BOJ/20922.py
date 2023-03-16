import sys

def get_answer(N, K, numbers):
    records = [0] * 100001
    max_partial_length = 0
    left_idx = 0

    for right_idx in range(N):
        num = numbers[right_idx]
        if records[num] == K:
            max_partial_length = max(max_partial_length, right_idx - left_idx)
            while numbers[left_idx] != numbers[right_idx]:
                records[numbers[left_idx]] -= 1
                left_idx += 1
            left_idx += 1
            records[num] -= 1
        records[num] += 1

    max_partial_length = max(max_partial_length, N - left_idx)
    return max_partial_length

def sol():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    numbers = list(map(int, input().split()))
    answer = get_answer(N, K, numbers)
    print(answer)

def test():
    TEST_CASES = [
        ["9 2", "3 2 5 5 6 4 4 5 7", 7],
        ["10 1", "1 2 3 4 5 6 6 7 8 9", 6],
        ["29 3", "1 2 3 4 5 6 7 8 9 1 1 11 1 14 15 16 23 43 24 53 24 25 99 29 36 45 64 69 45", 28],
        ["16 3", "1 2 3 4 5 6 7 8 9 1 1 11 1 2 2 2", 14],
        ["10 3", "1 2 3 4 5 6 7 1 1 1", 9],
        ["10 3", "1 1 1 1 1 1 1 1 1 1", 3],
        ["10 3", "1 1 1 2 2 1 1 1 1 1", 5],
        ["21 1", "1 2 3 4 5 6 6 7 8 9 10 11 13 15 63 34 34 33 33 22 1", 10],
        ["21 2", "1 2 3 2 3 1 4 4 4 5 6 7 8 9 9 8 7 6 5 2 1", 14]
    ]
    failed_case = 0
    for (i, case) in enumerate(TEST_CASES):
        N, K = map(int, case[0].split())
        numbers = list(map(int, case[1].split()))
        expected_answer = int(case[2])
        answer = get_answer(N, K, numbers)
        if answer != expected_answer:
            print(f'#{i+1} test case has been failed: the expected answer is {expected_answer} but {answer} is given')
            failed_case += 1
    if failed_case > 0:
        exit(0)

test()
sol()