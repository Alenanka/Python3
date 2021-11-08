#  Есть два списка:
# tutors = [
#     'Иван', 'Анастасия', 'Петр', 'Сергей',
#     'Дмитрий', 'Борис', 'Елена'
# ]
# klasses = [
#     '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
# ]
# Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:
# ('Иван', '9А')
# ('Анастасия', '7В')

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Сергей', ' Анастасия']
klasses = ['9А', '7В', '9Б', '9В']


def gen_tutor_klases_v1():
    if len(tutors) > len(klasses):
        while len(tutors) > len(klasses):
            klasses.append(None)
    return ((t, k) for t, k in zip(tutors, klasses))


g = gen_tutor_klases_v1()
print(type(g))
print(*g)


def gen_tutor_klases_v2():
    i = 0
    while i < len(tutors):
        if i < len(klasses):
            yield (tutors[i], klasses[i])
            i += 1
        else:
            yield (tutors[i], None)
            i += 1


gen = gen_tutor_klases_v2()
print(gen)
for i in gen:
    print(i)
