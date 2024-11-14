class Vehicle:
    __COLOR_VARIANTS = ['red', 'yellow', 'green', 'blue']

    def __init__(self, owner: str, __model: str, __engine_power: int, __color: str):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self. __color =  __color

    def get_model(self):
        return (f'Модель: {self.__model}')

    def get_horsepower(self):
        return (f'Мощность двигателя: {self.__engine_power}')

    def get_color(self):
        return (f'Цвет: {self.__color}')

    def print_info(self):
        print(f'Модель:{self.owner}, Мощность двигателя: {self.__engine_power}, Цвет: {self.__color}, Владелец: {self.owner}')

    def set_color(self, new_color: str):
        if new_color in Vehicle.__COLOR_VARIANTS:
            self.__color = new_color
            print(f'Цвет изменен на {self.__color}')
        else:
            print(f'Нельзя сменить цвет на {new_color}')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

vehicle = Vehicle("Иван", "Toyota Camry", 200, "red")
print(vehicle.get_model())
print(vehicle.get_horsepower())
print(vehicle.get_color())
vehicle.print_info()
vehicle.set_color("blue")
vehicle.set_color("purple")

sedan = Sedan("Алексей", "Honda Accord", 250, "yellow")
sedan.print_info()

