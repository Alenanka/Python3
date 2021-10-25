# Создать список, содержащий цены на товары (10–20 товаров), например:[57.8, 46.51, 97, ...]
# Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп
# (например «5 руб 04 коп»). Подумать, как из цены получить рубли и копейки, как добавить нули, если,
# например, получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).

price = [17.12, 46.8, 97, 45.6, 34, 1, 1004, 2.3, 34, 54, 56.7]

# вариант 1
price_with_format = []
for i in price:
    if isinstance(i, int):
        price_with_format.append('{0:02d} руб 00 коп'.format(i))
    else:
        price_with_format.append('{0:02d} руб {1:02d} коп'.format(int(i), int(str(i).split('.')[1])))
print(','.join(price_with_format))

# вариант 2

price_with_format = []
for i in price:
    if str(i).count('.'):
        price_with_format += ['{0:02d} руб {1:02d} коп'.format(int(i), int(str(i).split('.')[1]))]
    else:
        price_with_format += ['{0:02d} руб 00 коп'.format(i)]
print(','.join(price_with_format))


# cортировка, одинаковый id доказывает что объект списка после сортировки остался тот же
print(price, id(price))
price.sort()
print(price, id(price))

# создаем новый список и сортируем в обратном порядке
price = [17.12, 46.8, 97, 45.6, 34, 1, 1004, 2.3, 34, 54, 56.7]
print(price, id(price))
prices_new_sorted = sorted(price, reverse=True)
print(prices_new_sorted, id(prices_new_sorted))

# вывестити 5 самых дорогих товаров по возрастнию
print('5 самых дорогих товаров по возрастанию: ', sorted(sorted(price, reverse=True)[:5]))
