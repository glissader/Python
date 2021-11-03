# Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

# Продолжить работу над первым заданием.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.

# Продолжить работу над вторым заданием.
# Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

from enum import Enum


class OfficeEquipment:
    __name: str

    def __init__(self, name: str) -> None:
        self.__name = name

    def __str__(self) -> str:
        return self.__name


class PrinterType(Enum):
    LASER = 'laser'
    INJECT = 'inject'


class Printer(OfficeEquipment):
    __type: PrinterType

    def __init__(self, name: str, t: PrinterType) -> None:
        super().__init__(name)
        self.__type = t

    def __str__(self) -> str:
        return f'{super().__str__()} : {self.__type.value}'


class ScannerType(Enum):
    TABLET = 'tablet'
    FEED = 'feed'


class Scanner(OfficeEquipment):
    __type: ScannerType

    def __init__(self, name: str, t: ScannerType) -> None:
        super().__init__(name)
        self.__type = t

    def __str__(self) -> str:
        return f'{super().__str__()} {self.__type.value}'


class XeroxType(Enum):
    OFFICE = 'office'
    HOME = 'home'


class Xerox(OfficeEquipment):
    __type: XeroxType

    def __init__(self, name: str, t: XeroxType) -> None:
        super().__init__(name)
        self.__type = t

    def __str__(self) -> str:
        return f'{super().__str__()} {self.__type.value}'


class Warehouse:
    __items = {}

    def put(self, equipment: OfficeEquipment, count: int):
        try:
            int(count)
        except ValueError:
            return
        self.__items.update({equipment: count})

    def move_to(self, equipment: OfficeEquipment):
        v = self.__items.get(equipment)
        self.__items.update({equipment: v - 1})

    def __str__(self) -> str:
        return f'{self.__items}'


w = Warehouse()
printer = Printer('HP', PrinterType.LASER)
w.put(printer, 2)
scanner = Scanner('Canon', ScannerType.FEED)
w.put(scanner, 3)
xerox = Xerox('Canon', XeroxType.OFFICE)
w.put(xerox, 5)

print(w)
w.move_to(printer)
print(w)
w.put(xerox, 'd')
