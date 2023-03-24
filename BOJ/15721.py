import sys

def get_answer(A, T, t):
    n = 0
    cnt = [0, 0]

    while True:
        n += 1
        if cnt[t] + n + 3 >= T:
            break
        cnt[0] += n + 3
        cnt[1] += n + 3

    total = sum(cnt)
    track = [0, 1, 0, 1] + [0] * (n + 1) + [1] * (n + 1)

    for i in range(len(track)):
        total += 1
        if track[i] == 0:
            cnt[0] += 1
        else:
            cnt[1] += 1
        if cnt[t] == T:
            break

    return (total - 1) % A

def sol():
    input = sys.stdin.readline
    A = int(input())
    T = int(input())
    t = int(input())
    print(get_answer(A, T, t))

def test():
    cases = [
        [8, 2, 0, 2],
        [4, 6, 1, 3],
        [8, 8, 0, 5],
        [8, 8, 1, 0]
    ]

    for i, (A, T, t, expected) in enumerate(cases):
        answer = get_answer(A, T, t)
        if expected != answer:
            print(f'case #{i + 1} is wrong!\n{expected} is expected, but {answer} is given')

test()