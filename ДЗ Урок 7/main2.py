# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, name: str) -> None:
        self.__name = name

    def __str__(self) -> str:
        return f'{self.__name}'

    @abstractmethod
    def tissue_consumption(self) -> float:
        pass


class Coat(Clothes):

    def __init__(self, name: str, v: int) -> None:
        super().__init__(name)
        self.__v = v

    @property
    def tissue_consumption(self) -> float:
        return self.__v / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, name: str, h: int) -> None:
        super().__init__(name)
        self.__h = h

    @property
    def tissue_consumption(self) -> float:
        return 2 * self.__h + 0.3


c = Coat("Tall Coat", 27)
print(f'{c}: {c.tissue_consumption}')

s = Suit("Small Suit", 180)
print(f'{s}: {s.tissue_consumption}')
