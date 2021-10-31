# Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
# взятых из трёх списков (по одному из каждого):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#        Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]

from random import choice
def get_jokes(num):
    """
     Generates number of jokes formed from three random words

     :param num: number of jokes
     :return: list of jokes
     """
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    list_of_jokes = []
    for i in range(num):
        list_of_jokes.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')
    return list_of_jokes
num_of_jokes = input('Введите количество шуток :')
print(get_jokes(int(num_of_jokes)))
