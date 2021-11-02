# Реализуйте базовый класс Car.
# - у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# - опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# - добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# - для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.

from enum import Enum


class Direction(Enum):
    LEFT = 'left'
    RIGHT = 'right'
    FORWARD = 'forward'
    BACKWARD = 'backward'


class Car:
    def __init__(self, color: str, name: str, is_police: bool):
        self.__color = color
        self.__name = name
        self.__is_police = is_police
        self.speed = 0

    def show_speed(self):
        print(f'speed = {self.speed} km/h')

    def go(self):
        print("The car is running")
        return self

    def stop(self):
        print('The car is stopped')
        return self

    def turn(self, direction: Direction):
        print(f'The car is turned to the {direction.value}')
        return self

    def __str__(self) -> str:
        return f'{self.__name} {self.__color} {self.__is_police}'


class TownCar(Car):

    def __init__(self, color: str, name: str):
        super().__init__(color, name, False)

    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f'Speed {self.speed} is too high!')


class SportCar(Car):

    def __init__(self, color: str, name: str):
        super().__init__(color, name, False)


class WorkCar(Car):

    def __init__(self, color: str, name: str):
        super().__init__(color, name, False)

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f'Speed {self.speed} is too high!')


class PoliceCar(Car):

    def __init__(self, color: str, name: str):
        super().__init__(color, name, True)


town_car = TownCar(color='yellow', name='Volvo')
town_car.go().turn(Direction.LEFT)
town_car.speed = 100
town_car.show_speed()

police_car = PoliceCar(color='white', name='BMW')
police_car.go().turn(Direction.RIGHT)
police_car.speed = 90
police_car.show_speed()
