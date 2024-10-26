# success case
"""
memory effiecient
heap insertion time complexity: O(log n)
heap pop time complexity: O(log n)

main logic:
1. if length of heap is smaller than N, push the current number
2. if the current number is smaller than heap[0] then skip
3. if the current number is bigger than heap[0](which is the smallest number in the heap), replace pop the first element and push the number into the heap
4. print the first element in the heap
"""

import sys
import heapq

input = sys.stdin.readline

N = int(input())

result = []
for i in range(N):
    arr = list(map(int, input().split()))
    for e in arr:
        if len(result) < N:
            heapq.heappush(result, e)
            continue

        if result[0] < e:
            heapq.heapreplace(result, e)

print(result[0])


# out of memory case
"""
time complexity: O(N^2)
the reason this logic fails: out of memory, memory size of 1500^2 length of array is over 12 MB
"""


input = sys.stdin.readline

N = int(input())

sd_arr = [[0] * N for _ in range(N)]
for i in range(N):
    arr = list(map(int, input().split()))
    sd_arr[i] = arr

idx_arr = [N - 1 for _ in range(N)]
result = 0

for _ in range(N):
    ARR = [sd_arr[idx_arr[i]][i] for i in range(N)]
    max_value = max(ARR)
    idx_arr[ARR.index(max_value)] -= 1
    result=max_value

print(result)
