import sys
input = sys.stdin.readline

n, m = map(int, input().split())
cards = list(map(int, input().split()))

for _ in range(m):
    cards.sort()
    union = cards[0] + cards[1]
    cards[0], cards[1] = union, union

print(sum(cards))
