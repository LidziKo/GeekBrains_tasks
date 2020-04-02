class Road:

    def __init__(self, length, width):
        self.__length = length  # измеряется в метрах
        self.__width = width  # измеряется в метрах
        self.mass = 25  # измеряется в килограммах
        self.depth = 5  # измеряется в сантиметрах
        self.kilo_per_ton = 1000

    def calculate_asphalt_mass(self):
        result_mass = (self.__length * self.__width * self.mass * self.depth) / self.kilo_per_ton
        return result_mass


road = Road(4045, 20)
print(f'Масса асфальта, необходимого для покрытия всего дорожного полотна: {road.calculate_asphalt_mass()} тонн')
