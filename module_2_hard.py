n = int(input("Введите число от 3 до 20 включительно: "))
while n < 3 or n > 20:
    n = int(input("Ошибка, введите корректное число: "))
result = ""
sub_pairs = []
pairs = []
for i in range(1, 20):  # создание списка уникальных пар
    for j in range(i+1, 20):
        if j == i:
            continue
        sub_pairs.append(i)
        sub_pairs.append(j)
        pairs.append(sub_pairs)
        sub_pairs = []

for i in range(0, len(pairs)):  # проверка на кратность и заполнения списка с результатами
    if n % (pairs[i][0] + pairs[i][1]) == 0:
        result = result + str(pairs[i][0]) + str(pairs[i][1])
print("")
print(f'Пароль: {result}')
