import sys

def pop_A(T):
    return T[:-1]

def pop_B(T):
    return T[1:][::-1]

def answer(S, T):
    a, b = 0, 0
    if len(S) == len(T):
        return 1 if S == T else 0
    if T[-1] == 'A':
        a = answer(S, pop_A(T))
    if T[0] == 'B':
        b = answer(S, pop_B(T))

    if a == 1 or b == 1:
        return 1

    return 0

def sol():
    input = sys.stdin.readline
    S = input().strip()
    T = input().strip()
    print(answer(S, T))

sol()

def test():
    cases = [
        ['A', 'BABA', 1],
        ['BAAAAABAA', 'BAABAAAAAB', 1],
        ['A', 'ABBA', 0]
    ]

    for i, (S, T, expected) in enumerate(cases):
        result = answer(S, T)
        if result != expected:
            print(f'case #{i + 1} is wrong!\n{expected} is expected, but {result} is given')


test()

