import sys
input = sys.stdin.readline
cases = int(input())

for _ in range(cases):
    n = int(input())
    prices = list(map(int, input().split(' ')))
    profits = 0
    max = 0
    for i in range(n-1, -1, -1):
        if prices[i] > max:
            max = prices[i]
        else:
            profits += max - prices[i]

    print(profits)
  
