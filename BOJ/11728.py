import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
L = sorted(A + B)
print(' '.join(str(x) for x in L))