class Stationery:
    def draw(self):
        print('Рисуем чем то.')

class Pen(Stationery):
    def draw(self):
        print('Рисуем ручкой')

class Pencil(Stationery):

    def draw(self):
        print('Рисуем карандашом')

class Handle(Stationery):
    def draw(self):
        print('Рисуем маркером')

new_st = Stationery().draw()
new_pen = Pen().draw()
new_pencil = Pencil().draw()
new_handle = Handle().draw()
