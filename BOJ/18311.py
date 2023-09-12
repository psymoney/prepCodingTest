"""
link: https://www.acmicpc.net/problem/18311
title: 왕복
tier: silver 5
"""
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
lengths = list(map(int, input().split()))
courses = [i for i in range(0, N)] + [i for i in range(N - 1, -1, -1)]

for course in courses:
    length = lengths[course]
    K -= length
    if K < 0:
        print(course + 1)
        break
