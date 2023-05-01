def solve(n):
    t = 0

    for i in range(1, n + 1):
        if n - t > i:
            t += i
        elif n - t == i:
            return i
        elif n - t < i:
            return i - 1

def test():
    CASES = [
        [200, 19],
        [1, 1],
        [2, 1],
        [3, 2],
        [4, 2],
        [5, 2],
        [6, 3],
        [7, 3],
        [8, 3],
        [9, 3],
        [10, 4],
    ]

    for n, expected in CASES:
        result = solve(n)
        if result != expected:
            print(f'Wrong answer for {n}.\nExpected: {expected}\nReturned: {result}')

test()