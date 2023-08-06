import sys


input = sys.stdin.readline

N = int(input())
students = []

for i in range(N * N):
    students.append(list(map(int, input().split())))

table = [[0] * N for _ in range(N)]
satisfactions = [[0] * N for _ in range(N)]


def get_empty_adjacent_tables(row: int, col: int, t: list, n: int) -> int:
    empty_adjacent_tables = 0

    if row > 0 and t[row - 1][col] == 0:
        empty_adjacent_tables += 1
    if row < n - 1 and t[row + 1][col] == 0:
        empty_adjacent_tables += 1
    if col > 0 and t[row][col - 1] == 0:
        empty_adjacent_tables += 1
    if col < n - 1 and t[row][col + 1] == 0:
        empty_adjacent_tables += 1

    return empty_adjacent_tables


def get_interested_adjacent_tables(row: int, col: int, t: list, n: int, stu) -> int:
    interested_adjacent_tables = 0

    if row > 0 and t[row - 1][col] in stu[1:]:
        interested_adjacent_tables += 1
    if row < n - 1 and t[row + 1][col] in stu[1:]:
        interested_adjacent_tables += 1
    if col > 0 and t[row][col - 1] in stu[1:]:
        interested_adjacent_tables += 1
    if col < n - 1 and t[row][col + 1] in stu[1:]:
        interested_adjacent_tables += 1

    return interested_adjacent_tables


# O(N^2)
def allocate_student_at_table(student_data: list, t: list, n) -> None:
    temp = (0, 0, 0, 0)

    for row in range(n):
        for col in range(n):
            if t[row][col] != 0:
                continue

            empty_adjacent_tables = get_empty_adjacent_tables(row, col, t, n)
            interested_adjacent_tables = get_interested_adjacent_tables(row, col, t, n, student_data)

            if interested_adjacent_tables > temp[0]:
                temp = (interested_adjacent_tables, empty_adjacent_tables, row, col)
            elif interested_adjacent_tables == temp[0]:
                if empty_adjacent_tables > temp[1]:
                    temp = (interested_adjacent_tables, empty_adjacent_tables, row, col)
                elif empty_adjacent_tables == temp[1]:
                    if row < temp[2]:
                        temp = (interested_adjacent_tables, empty_adjacent_tables, row, col)
                    elif row == temp[2] and col < temp[3]:
                        temp = (interested_adjacent_tables, empty_adjacent_tables, row, col)

    t[temp[2]][temp[3]] = student_data[0]


# O(N^4)
def allocates(std, t, n) -> None:
    for student in std:                             # O(N^2)
        allocate_student_at_table(student, t, n)    # O(N^2)


#O(N^4)
def calculate_satisfaction_table(std, t, n, s) -> None:
    total = 0
    for row in range(n):
        for col in range(n):
            idx = 0
            for i in range(len(std)):
                if std[i][0] == t[row][col]:
                    idx = i
                    break

            interested = get_interested_adjacent_tables(row, col, t, n, std[idx])
            satisfaction = 0

            if interested == 4:
                satisfaction = 1000
            elif interested == 3:
                satisfaction = 100
            elif interested == 2:
                satisfaction = 10
            elif interested == 1:
                satisfaction = 1

            s[row][col] = satisfaction
            std.pop(idx)


allocates(students, table, N)
calculate_satisfaction_table(students, table, N, satisfactions)

total = 0
for y in range(N):
    total += sum(satisfactions[y])

print(total)
