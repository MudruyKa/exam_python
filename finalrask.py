import random

# Генерация исходного списка
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)

# Перевод в one hot вид
unique_values = list(set(lst))
one_hot_encoded = []

for item in lst:
    one_hot_row = [1 if item == value else 0 for value in unique_values]
    one_hot_encoded.append(one_hot_row)

# Форматируем результат в читаемую таблицу
header = ["whoAmI"] + unique_values
table = [[lst[i]] + one_hot_encoded[i] for i in range(len(lst))]

# Печать таблицы
print(header)
for row in table[:5]:  # Показываем только первые 5 строк для краткости
    print(row)
