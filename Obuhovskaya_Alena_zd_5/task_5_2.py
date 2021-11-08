# Решить задачу генерации нечётных чисел от 1 до n (включительно),
# не используя ключевое слово yield.

n = int(input('Введите число:'))

gen_odd = (i for i in range(1, n+1, 2))

print(type(gen_odd))
for i in gen_odd:
    print(i)
