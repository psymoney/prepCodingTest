"""
link: https://www.acmicpc.net/problem/3085
title: 사탕 게임
tier: silver 2
"""
import sys
input = sys.stdin.readline

N = int(input().rstrip())
board = [list(str(input().rstrip())) for _ in range(N)]

D = [(0, -1), (0, 1), (-1, 0), (1, 0)]
answer = 0


def count_same_color_candy_in_x_axis(x, y):
    color = board[y][x]
    streak = 0
    count = 0

    for i in range(N):
        if board[y][i] == color:
            count += 1
        else:
            streak = max(count, streak)
            count = 0

    return max(count, streak)


def count_same_color_candy_in_y_axis(x, y):
    color = board[y][x]
    streak = 0
    count = 0

    for i in range(N):
        if board[i][x] == color:
            count += 1
        else:
            streak = max(count, streak)
            count = 0

    return max(count, streak)


def check_initial_max():
    for y in range(N):
        if y == 0:
            for x in range(N):
                if count_same_color_candy_in_y_axis(x, y) == N:
                    return True
        if count_same_color_candy_in_x_axis(0, y) == N:
            return True
    return False


if check_initial_max():
    answer = N
else:
    # compare with candy from up, down, left, and right -> if two candies are the same color then pass
    for y in range(N):
        for x in range(N):
            for dx, dy in D:
                nx, ny = x + dx, y + dy
                if nx in range(N) and ny in range(N):
                    if board[ny][nx] != board[y][x]:
                        # switch -> save switched axis sets for rollback
                        board[ny][nx], board[y][x] = board[y][x], board[ny][nx]

                        # count from x-axis change
                        answer = max(answer, count_same_color_candy_in_x_axis(x, y))
                        answer = max(answer, count_same_color_candy_in_x_axis(nx, ny))

                        # count from y-axis change
                        answer = max(answer, count_same_color_candy_in_y_axis(x, y))
                        answer = max(answer, count_same_color_candy_in_y_axis(nx, ny))

                        # rollback switch
                        board[ny][nx], board[y][x] = board[y][x], board[ny][nx]

print(answer)

