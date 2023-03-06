formular = list(input().split('-'))
total = 0

for i in range(len(formular)):
    partial_sum = sum(list(map(int, formular[i].split('+'))))
    if i == 0:
        total += partial_sum
    else:
        total -= partial_sum

print(total)