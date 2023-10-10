import sys



def b_search(target, data):
    start = 0
    end = len(data) - 1
    while start <= end:
        mid = (start + end) // 2
        if data[mid] == target:
            return 1
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid -1
    return 0


def sol():
    input = sys.stdin.readline
    N = int(input())
    A = sorted(list(map(int, input().split())))
    M = int(input())
    m = list(map(int, input().split()))
    for e in m:
        print(b_search(e, A))