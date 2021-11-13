# Представлен список чисел. Необходимо вывести те его элементы,
# значения которых больше предыдущего, например:
# src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55,56]
# result = [12, 44, 4, 10, 78, 123]
# ```
#
# Подсказка: использовать возможности python, изученные на уроке.

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55, 56]

# вариант 2

result = []
for i in range((len(src))-1):
    if src[i+1] > src[i]:
        result.append(src[i+1])
print(result)

# вариант 2

res = [src[i+1] for i in range((len(src))-1) if src[i+1] > src[i]]
print(res)