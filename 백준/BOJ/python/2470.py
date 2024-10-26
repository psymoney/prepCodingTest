import sys

def get_combination(materials):
    L = 0
    R = len(materials) - 1

    materials.sort()
    min_comb = (materials[L], materials[R])


    while L < R:
        DL = abs(materials[L+1] + materials[R])
        DR = abs(materials[L] + materials[R-1])
        if abs(materials[L] + materials[R]) < abs(sum(min_comb)):
            min_comb = (materials[L], materials[R])
        if DL < DR:
            L += 1
        else:
            R -= 1

    return min_comb

def sol():
    input = sys.stdin.readline
    N = int(input())
    print(" ".join(str(x) for x in get_combination(list(map(int, input().split())))))

def test():
    cases = [
        ("-2 4 -99 -1 98", "-99 98"),
        ("-87 -42 -40 -22 -11 23 29 78 79 98", "-22 23"),
        ("-99 -98 1 0 96", "0 1"),
        ("-8 -1 -3 -10 -9 -5 -4 -2 -7 -6", "-2 -1"),
        ("-10 1 2", "1 2"),
        ("999999995 999999996 999999997 1000000000", "999999995 999999996"),
        ("1000000000 1000000000", "1000000000 1000000000")
    ]

    for i, (case, answer) in enumerate(cases):
        result = " ".join(str(x) for x in get_combination(list(map(int, case.split()))))
        if result != answer:
            print(f'case #{i+1} is wrong!\nanswer is {answer}, but {result} is given')

if __name__ == "__main__":
    DEBUG = False
    if DEBUG:
        test()
    sol()
