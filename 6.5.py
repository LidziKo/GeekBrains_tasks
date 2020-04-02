class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'{self.title}: запуск отрисовки...')


class Pen(Stationery):
    def draw(self):
        super().draw()
        print('Прорисовка контура')


class Pencil(Stationery):
    def draw(self):
        super().draw()
        print('Наложение теней')


class Handle(Stationery):
    def draw(self):
        super().draw()
        print('Заполнение областей цветом')


green_pen = Pen('Зелёная ручка')
ordinary_pencil = Pencil('Обычный карандаш')
pink_handle = Handle('Розовый маркер')


green_pen.draw()
ordinary_pencil.draw()
pink_handle.draw()
