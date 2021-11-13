# Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.
# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать из этих элементов список с сохранением порядка их следования в исходном списке,
# например:
# src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]
# Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации.

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# решение в лоб

unique = []
for i in range(len(src)):
    if src.count(src[i]) < 2:
        unique.append(src[i])
print(unique)

# оптимизировано

unique_compr = [src[i] for i in range(len(src)) if src.count(src[i]) < 2]
print(unique_compr)

# через множества

unique_set = set()
tmp = set()
for el in src:
    if el not in tmp:
        unique_set.add(el)
    else:
        unique_set.discard(el)
    tmp.add(el)
unique_brands_ord = [el for el in src if el in unique_set]
print(unique_brands_ord)