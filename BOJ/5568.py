import sys
from itertools import permutations

def answer(cards, k):
    numbers = set()
    cases = permutations(cards, k)

    for case in cases:
        numbers.add(int("".join(map(str, case))))

    return len(numbers)

def sol():
    input = sys.stdin.readline
    N = int(input())
    K = int(input())
    cards = [int(input()) for _ in range(N)]

    print(answer(cards, K))

sol()

def test():
    test_cases = [
        ([1, 2, 12, 1], 2, 7),
        ([72, 2, 12, 7, 2, 1], 3, 68)
    ]

    for i, (cards, k, expected) in enumerate(test_cases):
        result = answer(cards, k)
        if result != expected:
            print(f'case #{i+1} is wrong!\n{expected} is expected, but {result} is given')

test()