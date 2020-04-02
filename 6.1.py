import time


class TrafficLights:

    def __init__(self, color):
        self.__color = ['red', 'yellow', 'green', 'yellow']
        try:
            self.start = self.__color.index(color)
        except ValueError:
            self.start = 0
        self.timer = [5, 1, 3, 1]

    def running(self):
        while True:
            print(self.__color[self.start])
            time.sleep(self.timer[self.start])
            self.start += 1
            if self.start >= len(self.__color):
                self.start = 0


tr_lght = TrafficLights('green')
tr_lght.running()
