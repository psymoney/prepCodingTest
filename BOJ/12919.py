import sys

def append_A(S):
    return S + "A"

def append_B(S):
    return "B" + S[::-1]

def answer(S, T):
    if len(S) == len(T):
        return 1 if S == T else 0

    a = answer(append_A(S), T)
    b = answer(append_B(S), T)

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

