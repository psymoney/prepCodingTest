"""
문제 해결 접근 방법:
1. 월, 일의 조합을 일 단위 정수로 환산, 길이로 치환해 선으로 표현한다. (x, y)
2. 개화일을 기준으로 오름차순 정렬한다.
3. 3월 1일에 해당하는 길이를 초기값으로 갖는 기준점보다 개화일이 빠른 부분 집단을 순회한다.
    3-1. 부분 집단 중 낙화 시기가 가장 늦는 대상을 찾고 해당 값을 기준점으로 갱신한다.
    3-2. 기준점보다 개화시기가 빠른 부분 집단이 존재하지 않는 경우, 프로세스 종료
"""

import sys
input = sys.stdin.readline

DEBUG = False

DAYS = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
MONTH_IN_DAYS = [0] * 13
for i in range(1, 13):
    MONTH_IN_DAYS[i] = MONTH_IN_DAYS[i-1] + DAYS[i-1]
PERIOD = [MONTH_IN_DAYS[3], MONTH_IN_DAYS[11] + DAYS[11]]

if DEBUG:
    print(PERIOD)

N = int(input())
F = [[] for _ in range(N)]
for i in range(N):
    period = list(map(int, input().split()))
    F[i] = [MONTH_IN_DAYS[period[0]] + period[1], MONTH_IN_DAYS[period[2]] + period[3]]
F.sort(key=lambda x: x[0])
if DEBUG:
    print(F)

cnt = 0
i = 0

while i < N:
    if DEBUG:
        print(f'i = {i}')
    m = 0
    if F[i][0] <= PERIOD[0] < F[i][1]:
        max_fall_day = F[i][1]
        m = i
        for j in range(i+1, N):
            if F[j][0] <= PERIOD[0] and F[j][1] > max_fall_day:
                max_fall_day = F[j][1]
                m = j
            if F[j][0] > PERIOD[0]:
                break
        PERIOD[0] = max_fall_day
        cnt += 1

        if DEBUG:
            print(f'selected this index = {m}')
    elif F[i][1] <= PERIOD[0]:
        i += 1
    else:
        cnt = 0
        break
    if F[m][1] > PERIOD[1]:
        break
    i = m + 1

print(cnt)