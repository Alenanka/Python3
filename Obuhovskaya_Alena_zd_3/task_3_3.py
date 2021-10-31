# Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и
# возвращающую словарь, в котором ключи — первые буквы имён,
# а значения — списки, содержащие имена, начинающиеся с соответствующей буквы. Например:
# >>> thesaurus("Иван", "Мария", "Петр", "Илья")
# {
#    "И": ["Иван", "Илья"],
#    "М": ["Мария"],
#    "П": ["Петр"]
# }
# Подумайте: полезен ли будет вам оператор распаковки? Как поступить, если потребуется
# сортировка по ключам? Можно ли использовать словарь в этом случае?

def thesaurus(*names):
    print(names)
    vocabl ={}
    for name in names:
        first_letters = name[0]
        vocabl.setdefault(first_letters, [])
        vocabl[first_letters].append(name)
    return vocabl

vocabl_name = thesaurus("Иван", "Петр","Мария", "Маия", "Илья")
print(vocabl_name)

# сортировка по ключам
vocabl_key = sorted(vocabl_name.keys())
for i in vocabl_key:
    print(i,':', vocabl_name[i])