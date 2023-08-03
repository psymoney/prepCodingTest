import sys


def answer(s: str, t: str) -> str:
    ps = 0

    for pt in range(len(t)):
        if ps == len(s):
            break
        if t[pt] == s[ps]:
            ps += 1

    return 'Yes' if ps == len(s) else 'No'


def solve():
    input = sys.stdin.readline
    while True:
        try:
            s, t = input().split()
            print(answer(s, t))
        except:
            break


def test():
    test_cases = [
        ['sequence', 'subsequence', 'Yes'],
        ['person', 'compression', 'No'],
        ['VERDI', 'vivaVittorioEmanueleReDiItalia', 'Yes'],
        ['caseDoesMatter', 'CaseDoesMatter', 'No'],
    ]

    for (i, case) in enumerate(test_cases):
        if answer(case[0], case[1]) != case[2]:
            print(f'Test case #{i+1} failed')


if __name__ == '__main__':
    test()
    solve()
