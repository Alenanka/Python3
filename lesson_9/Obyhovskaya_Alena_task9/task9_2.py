# Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина * ширина * масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см * число см толщины полотна;
# проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.

class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width
        print(self._width, self._length)

    def bitum_calc(self, weight_butum_on_cm, thickness):
        return self._length * self._width * weight_butum_on_cm * thickness / 1000


# if __name__ == '__main__':
while True:
    try:
        weight_butum_on_cm = float(input('Введите сколько альфальта необзодимо на толщину 1 см: '))
        break
    except ValueError as e:
        print('Ожидаем число')
while True:
    try:
        thickness = float(input('Введите желаемую толщину: '))
        break
    except ValueError as e:
        print('Ожидаем число')

r = Road(20.7, 5000)
print(f'Необходимо {r.bitum_calc(weight_butum_on_cm,thickness) } тонн асфальта')

