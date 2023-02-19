import sys
input = sys.stdin.readline

def fill_part_strs(str, part_strs, max_com_len):
    for i in range(len(str)):
        for (l, j) in enumerate(range(i+1, max_com_len)):
            # print(f'i = {i} / j = {j} / str_1[i:j] = {str_1[i:j]} / l = {l}')
            try:
                part_strs[l+1].index(str[i:j])
                continue
            except ValueError:
                part_strs[l+1].append(str[i:j])

def solution(part_strs_1, part_strs_2, max_com_len):
    for i in range(max_com_len - 1, -1, -1):
        for j in range(len(part_strs_1[i])):
            try:
                part_strs_2[i].index(part_strs_1[i][j])
                return i

            except ValueError:
                continue


str_1 = input()
str_2 = input()

max_com_len = len(str_1) if len(str_1) < len(str_2) else len(str_2)
part_strs_1 = [[' ']] + [[] for _ in range(max_com_len - 1)]
part_strs_2 = [[' ']] + [[] for _ in range(max_com_len - 1)]

fill_part_strs(str_1, part_strs_1, max_com_len)
fill_part_strs(str_2, part_strs_2, max_com_len)

print(solution(part_strs_1, part_strs_2, max_com_len))

