import sys
input = sys.stdin.readline

def multiply(a, b):
    n = len(a)
    result = [[0] * n for _ in range(n)]

    for row in range(n):
        for col in range(n):
            value = 0
            for i in range(n):
                value += a[row][i] * b[i][col]
            result[row][col] = value % 1000

    return result

def square(a, b):
    if b == 1:
        L = len(a)
        for row in range(L):
            for col in range(L):
                a[row][col] = a[row][col] % 1000
        return a

    sub_result = square(a, b // 2)

    if b % 2:
        return multiply(multiply(sub_result, sub_result), a)
    else:
        return multiply(sub_result, sub_result)

def print_matrix(matrix):
    for col in matrix:
        column = ''
        for row in col:
            column += f'{row} '
        print(column.strip())

N, B = list(map(int, input().split()))

A = []
for row in range(N):
    A.append(list(map(int, input().split())))

A_squared_B = square(A, B)
print_matrix(A_squared_B)

