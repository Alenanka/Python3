# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты:
#
# speed, color, name, is_police(булево).

# А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда);

# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.
class Car:

    def __init__(self, speed, color, name, ispolice=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.ispolice = ispolice

    def go(self):
        print(f'Автомобиль {self.name} начал движение')

    def stop(self):
        print(f'Автомобиль {self.name} остановился')

    def turn(self, direction):
        print(f'Автомобиль {self.name} поворачивает {direction}')

    def show_speed(self):
        print(f'Тукущая скорость автомобиля {self.name} {self.speed} км/ч')

class TownCar(Car):
    nax_speed = 60

    def show_speed(self):
        if self.speed > self.max_speed:
            print(
                f'Cкорость рабочего автомобилья превышена {self.name}: {self.speed}км/ч, разрешена не более {self.max_speed}')
        else:
            print(f'Текущая скорость автомобилья {self.name}: {self.speed}км/ч')

class SportCar(Car):
    def __init__(self, speed, color, name, ispolice ):
        super().__init__(speed, color, name, ispolice)



class WorkCar(Car):
    max_speed = 40

    def show_speed(self):
        if self.speed > self.max_speed:
             print(f'Cкорость рабочего автомобилья превышена {self.name}: {self.speed}км/ч, разрешена не более {self.max_speed}')
        else:
            print(f'Текущая скорость автомобилья {self.name}: {self.speed}км/ч')


class PoliceCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


tc1 = TownCar(190, 'Silver', 'Rang Rover')
print(tc1.ispolice)
tc1.go()
tc1.turn('налево')
tc1.stop()

pc = PoliceCar(60, 'blue', 'pol3456')
pc.go()
pc.turn('Налево')
pc.show_speed()
pc.stop()
print(pc.ispolice)

wc = WorkCar(80, 'green', 'WorkCar')
wc.go()
wc.show_speed()