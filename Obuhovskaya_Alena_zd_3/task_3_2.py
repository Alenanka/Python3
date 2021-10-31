def num_translate_adv(ingl_num):
    vocabl_of_numbers = {
        'zero': 'ноль',
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять'
    }
    if ingl_num.istitle():
        print(vocabl_of_numbers.get(ingl_num.lower()).title())
    else:
        print(vocabl_of_numbers.get(ingl_num))

num_translate_adv(input('Введите число  на английском от 1 до 10 прописью: '))

