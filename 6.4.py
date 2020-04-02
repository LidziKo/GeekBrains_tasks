class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('автомобиль начал движение')

    def stop(self):
        print('автомобиль остановился')

    def turn(self, direction):
        print(f'автомобиль повернул {direction}')

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.speed}')


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)
        self.max_speed = 60

    def show_speed(self):
        if self.max_speed > self.speed:
            super().show_speed()
        else:
            print('Превышение скорости!')


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)
        self.max_speed = 40

    def show_speed(self):
        if self.max_speed > self.speed:
            super().show_speed()
        else:
            print('Превышение скорости!')


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


pickup = WorkCar(90, 'red', 'toyota')

pickup.show_speed()
pickup.turn('налево')
print(pickup.is_police)
print(pickup.name)
pickup.stop()

police = PoliceCar(180, 'white / blue', 'lada')
police.turn('направо')
print(police.is_police)
police.stop()
print(police.name)
