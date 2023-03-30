import sys

def get_answer(N, L):
    n = str(N)
    L.sort(reverse=True)
    answer = ""
    is_less = False

    for i in range(len(n)):
        num = int(n[i])
        if i == 0 and len(n) > 2 and len(L) == 1:
            is_less = True
            continue
        for e in L:
            if is_less:
                answer += str(e)
                is_less = False
                break
            else:
                if e > num:
                    continue
                elif e == num:
                    is_less = False
                else:
                    is_less = True
                answer += str(e)
                break

    return int(answer)

def test():
    cases = [
        # [657, [1, 5, 7], 577],
        # [111, [1], 11],
        [100000000, [1], 11111111]
    ]

    for i, (N, L, expected) in enumerate(cases):
        result = get_answer(N, L)
        if result != expected:
            print(f'case #{i+1} is wrong!\n{expected} is expected, but {result} is given')

test()

def sol():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    L = list(map(int, input().split()))

    print(get_answer(N, L))


sol()


