class Clothes:

    def __init__(self, name):
        self.name = name


class Coat(Clothes):

    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    @property
    def tissue_consumption(self):
        return self.size / 6.5 + 0.5

    @tissue_consumption.setter
    def tissue_consumption(self, value): # считает размер вещи, которую можно сделать из имеющейся длины ткани
        self.size = (value - 0.5) * 6.5


class Costume(Clothes):

    def __init__(self, name, height):
        super().__init__(name)
        self.height = height

    @property
    def tissue_consumption(self):
        return 2 * self.height + 0.3

    @tissue_consumption.setter
    def tissue_consumption(self, value):  # считает длину костюма, которую можно сделать из имеющейся длины ткани
        self.height = (value - 0.3) / 2


red_costume = Costume('red cost', 48)
blue_coat = Coat('blue coat', 130)

print(red_costume.tissue_consumption, blue_coat.tissue_consumption)

red_costume.tissue_consumption = 96.3
blue_coat.tissue_consumption = 20.5

print(red_costume.height, blue_coat.size)
