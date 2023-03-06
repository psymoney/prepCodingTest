formular = input()
prev = len(formular)
summand = 0

for i in range(prev - 1, -1, -1):
    if formular[i] == '+' or (i == 0 and formular[i] != '-'):
        summand += int(formular[i:prev])
        prev = i
    elif formular[i] == '-':
        operator = int(formular[i:prev])
        summand = min((abs(operator) + summand) * -1, operator + summand)
        prev = i

print(summand)