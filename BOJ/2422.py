import sys

def get_good_combos(N, A):
    combos = 0
    for a in range(1, N - 1):
        for b in range(a + 1, N):
            if b in A[a]:
                continue
            for c in range(b + 1, N + 1):
                if c in A[a] or c in A[b]:
                    continue
                combos += 1
    return combos

def sol():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    A = {x: [] for x in range(1, N+1)}
    for x in range(M):
        a, b = map(int, input().split())
        A[a].append(b)
        A[b].append(a)
    print(get_good_combos(N, A))

sol()

def test():
    cases = [
        (5, 3, {1:[2, 3], 2:[1], 3: [1, 4], 4:[3], 5:[], 6:[], 7:[]}, 3),
        (4, 1, {1:[4], 2:[], 3:[], 4:[1]}, 2)
    ]

    for i, (N, M, A, expected) in enumerate(cases):
        result = get_good_combos(N, A)
        if result != expected:
            print(f'case #{i + 1} is wrong!\n{expected} is expected, but {result} is given')

# test()

