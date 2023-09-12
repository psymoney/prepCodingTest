"""
link: https://www.acmicpc.net/problem/18311
title: 왕복
tier: silver 5
"""
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
lengths = [0] + list(map(int, input().split()))

total_length = sum(lengths)
course = 0

if K >= total_length:
    K -= total_length
    course = 6

    while K >= 0:
        course -= 1
        length = lengths[course]
        K -= length
else:
    course = 0

    while K >= 0:
        course += 1
        length = lengths[course]
        K -= length

print(course)
