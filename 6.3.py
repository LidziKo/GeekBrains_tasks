class Worker:

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = {'wage': 0,
                         'bonus': 0}

    def set_income_wage(self, value):
        self.__income['wage'] = value

    def get_income_wage(self):
        return self.__income['wage']

    def set_income_bonus(self, value):
        self.__income['bonus'] = value

    def get_income_bonus(self):
        return self.__income['bonus']


class Position(Worker):

    def __init__(self, name, surname, position):
        super().__init__(name, surname, position)

    def get_full_name(self):
        full_name = (self.name + ' ' + self.surname)
        return full_name

    def get_total_income(self):
        return self.get_income_wage() + self.get_income_bonus()


worker1 = Position('Vasya', 'Pupkin', 'Analyst')
worker1.set_income_wage(100500)
worker1.set_income_bonus(9000)
print(f'Сотрудник {worker1.get_full_name()} имеет заработную плату {worker1.get_total_income()} руб.')
