import sys
read = sys.stdin.readline

N = int(read())
A = list(map(int, read().split()))
lis = [A[0]]


def b_search(t):
    l, r = 0, len(lis) - 1

    while l < r:
        m = (l + r) // 2

        if e > lis[m]:
            l = m + 1
        else:
            r = m

    return r


for e in A[1:]:
    if e > lis[-1]:
        lis.append(e)
    else:
        i = b_search(e)
        lis[i] = e

print(len(lis))


