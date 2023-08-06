import sys


class SharkSchool:
    N: int = None
    students: list = None
    table: list = None
    satisfactions: list = None

    dr: list = [-1, 1, 0, 0]
    dc: list = [0, 0, -1, 1]

    def __init__(self):
        pass

    def initiate_properties(self) -> None:
        input = sys.stdin.readline
        self.N = int(input())
        self.students = [list(map(int, input().split())) for _ in range(self.N ** 2)]
        self.table = [[0] * self.N for _ in range(self.N)]
        self.satisfactions = [[0] * self.N for _ in range(self.N)]

    def solve(self):
        self.initiate_properties()
        self.allocates()
        print(self.total_satisfaction)

    # O(N^4)
    def allocates(self) -> None:
        for std in self.students:                  # O(N^2)
            self.allocate_student_at_table(std)    # O(N^2)

    # O(N^4)
    @property
    def total_satisfaction(self) -> int:
        total_satisfaction: int = 0
        students: list = sorted(self.students)

        for row in range(self.N):
            for col in range(self.N):
                idx = self.table[row][col] - 1

                empty, interested = self.get_empty_and_interested_adjacent_tables(row, col, students[idx])
                satisfaction = 10 ** (interested - 1) if interested != 0 else 0

                total_satisfaction += satisfaction

        return total_satisfaction

    # O(N^2)
    def allocate_student_at_table(self, stu: list) -> None:
        temp = (0, 0, 0, 0)  # respectively interested seats, empty seats, row, and column

        for row in range(self.N):
            for col in range(self.N):
                if self.table[row][col] != 0:
                    continue

                empty_tables, interested_tables = self.get_empty_and_interested_adjacent_tables(row, col, stu)

                if interested_tables > temp[0]:
                    temp = (interested_tables, empty_tables, row, col)
                elif interested_tables == temp[0]:
                    if empty_tables > temp[1]:
                        temp = (interested_tables, empty_tables, row, col)
                    elif empty_tables == temp[1]:
                        if row < temp[2]:
                            temp = (interested_tables, empty_tables, row, col)
                        elif row == temp[2] and col < temp[3]:
                            temp = (interested_tables, empty_tables, row, col)

        self.table[temp[2]][temp[3]] = stu[0]

    def get_empty_and_interested_adjacent_tables(self, row: int, col: int, std: list) -> tuple:
        empty_tables, interested_tables = 0, 0

        for i in range(4):
            nr, nc = row + self.dr[i], col + self.dc[i]

            if 0 <= nr < self.N and 0 <= nc < self.N:
                if self.table[nr][nc] == 0:
                    empty_tables += 1
                elif self.table[nr][nc] in std[1:]:
                    interested_tables += 1

        return empty_tables, interested_tables


if __name__ == '__main__':
    SharkSchool().solve()
