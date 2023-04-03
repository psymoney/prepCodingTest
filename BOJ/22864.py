
def answer(A, B, C, M):
    fatigue = 0
    works = 0

    for _ in range(24):
        if fatigue + A <= M:
            fatigue += A
            works += B
        else:
            fatigue = max(0, fatigue - C)

    return works

def test():
    cases = [
        [(5, 3, 2, 10), 24],
        [(10, 5, 1, 10), 15],
        [(11, 5, 1, 10), 0]
    ]

    for i, (args, expected) in enumerate(cases):
        result = answer(*args)
        if result != expected:
            print(f'case #{i+1} is wrong!\n{expected} is expected, but {result} is given')

def sol():
    args = map(int, input().split())
    print(answer(*args))

sol()

