from collections import deque

def answer(N, M):
    Q = deque()
    nums = []
    for i in range(1, N+1):
        nums.append(i)
        Q.append([i])

    while Q:
        comb = Q.popleft()
        if len(comb) == M:
            print(*comb)
        for num in nums:
            if num not in comb:
                Q.append(comb + [num])


def sol():
    N, M = map(int, input().split())
    answer(N, M)


if __name__ == '__main__':
    sol()
