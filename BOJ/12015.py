import sys
read = sys.stdin.readline

N = int(read())
A = list(map(int, read().split()))
lis = [A[0]]

for e in A[1:]:
    if e > lis[-1]:
        lis.append(e)
    else:
        l, r = 0, len(lis) - 1

        while l < r:
            m = (l + r) // 2

            if e > lis[m]:
                l = m + 1
            else:
                r = m

        lis[r] = e

print(len(lis))


