#  Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
#  Известно, что при хранении данных используется принцип: одна строка — один пользователь,
#  разделитель между значениями — запятая. Написать код, загружающий данные из обоих файлов и
#  формирующий из них словарь: ключи — ФИО, значения — данные о хобби. Сохранить словарь в файл.
#  Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО,
#  задаём в словаре значение None. Если наоборот — выходим из скрипта с кодом «1».
#  При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
# Фрагмент файла с данными о пользователях (users.csv):
# Иванов,Иван,Иванович
# Петров,Петр,Петрович
# Фрагмент файла с данными о хобби (hobby.csv):
# скалолазание,охота
# горные лыжи
import sys
import json

with open('users.csv', 'r', encoding='utf-8') as f:
    surnames = []
    for line in f:
        surnames.append((line.replace('\n', '').replace(',', ' ')))
with open('hobby.csv', 'r', encoding='utf-8') as f:
    hobbys = []
    for line in f:
        hobbys.append(line.replace('\n', ''))

if len(surnames) < len(hobbys):
    sys.exit(1)
else:
    for i in range(len(surnames)-len(hobbys)):
        hobbys.append(None)
    dict_hobby = dict(zip(surnames, hobbys))


with open('surname_hobby.csv', 'w', encoding='utf-8') as f:
    dict_hobby_as_str = json.dumps(dict_hobby)
    f.write(dict_hobby_as_str)

with open('surname_hobby.csv', 'r', encoding='utf-8') as f:
     hobby_surname_as_str = f.read()
hobby_surname = json.loads(hobby_surname_as_str)
print(hobby_surname)
