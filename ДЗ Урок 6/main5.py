# Реализовать класс Stationery (канцелярская принадлежность).
# - определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# - создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# - в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
# - создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title: str):
        self.__title = title

    def __str__(self) -> str:
        return self.__title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        super().draw()
        print('Ручка')


class Pencil(Stationery):
    def draw(self):
        super().draw()
        print('Карандаш')


class Handle(Stationery):
    def draw(self):
        super().draw()
        print('Маркер')


p = Pen(title='Gold pen')
p.draw()

c = Pencil(title='Black')
c.draw()

h = Handle(title='Yellow')
h.draw()
