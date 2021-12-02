import time

class TrafficLight:
    __сolors = {}

    def __init__(self):
       self.__сolors = {'Красный': 7, 'Желтый': 2, 'Зеленый': 5}

    def running(self):
        for key in self.__сolors:
            print(key)
            time.sleep(self.__сolors[key])

t = TrafficLight()
t.running()


