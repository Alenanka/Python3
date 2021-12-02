#  Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};

# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода
# с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров.

class Worker:

    def __init__(self, name, surname, position,wage,bonus ):
        self.name = name
        self.surname = surname
        self.position = position
        self._incom = {'wage': wage, 'bonus': bonus}

class Position(Worker):

    @property
    def get_full_name(self):
        return f'{self.surname} {self.name}'


    @property
    def get_total_income(self):
        return sum(self._incom.values())


p1 = Position('Alena', 'Abukhouskaya', 'ing', 155, 55)
p2 = Position('Maks', 'Reut', 'ing_1', 200, 0)
print(p2.name)
print(f'Полное имя сотрудника: {p1.get_full_name}')
print(f'Зарплата: {p1.get_total_income }  рублей')
p1.name = 'Kate'
p1._incom['bonus'] = 5
print(f'Полное имя сотрудника: {p1.get_full_name}')
print(f'Зарплата: {p1.get_total_income }  рублей')

print(f'Полное имя сотрудника: {p2.get_full_name}')
print(f'Зарплата: {p2.get_total_income} рублей')

