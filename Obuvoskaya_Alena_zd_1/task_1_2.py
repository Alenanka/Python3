odd_in_kub = []
sum_of_kub = 0
for i in range(1000):
    if i % 2:
        odd_in_kub .append(i**3)
for element_from_kub in odd_in_kub:
    number = element_from_kub
    sum_digit = 0
    while number > 0:
        digit = number % 10
        sum_digit += digit
        number = number // 10
    if not sum_digit % 7:
        sum_of_kub += element_from_kub
print('Cумма чисел из  списка, сумма цифр которых делится нацело на 7:', sum_of_kub)

sum_of_kub = 0
for element_from_kub in odd_in_kub:
    number = element_from_kub + 17
    sum_digit = 0
    while number > 0:
        digit = number % 10
        sum_digit += digit
        number = number // 10
    if not sum_digit % 7:
        sum_of_kub += element_from_kub + 17
print('Cумма чисел из  списка, сумма цифр которых делится нацело на 7 c добавлением числа 17 :', sum_of_kub)
