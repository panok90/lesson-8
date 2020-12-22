""""""

import sys


class CountError(Exception):
    def __init__(self, err):
        self.err = err

    def __str__(self):
        return self.err


class IntError(Exception):
    def __init__(self, err):
        self.err = err

    def __str__(self):
        return self.err


def control_int(count):
    try:
        if isinstance(count, str):
            raise IntError(f'Количество товара должно быть число!')
    except IntError as err:
        print(err)
        sys.exit(0)
    else:
        return count


class Warehouse:

    def __init__(self):
        self.list_goods = list()

    def add_goods(self, good, count):
        count = control_int(count)  # Проверка введеного колисества на тип данных
        dict_good = {good.name: good, 'count': count}
        self.list_goods.append(dict_good)

    def transfer_goods(self, good, count, division):
        count = control_int(count)  # Проверка введеного колисества на тип данных
        for item in range(len(self.list_goods)):
            if good.name in self.list_goods[item]:
                try:
                    if count > self.list_goods[item]["count"]:
                        raise CountError(f'На складе недостаточно товара:\n'
                                         f' {good.name}. -{count -self.list_goods[item]["count"]} шт.\n'
                                         f'Укажите корректное количество.')
                except CountError as err:
                    print(err)
                else:
                    if count == self.list_goods[item]["count"]:
                        self.list_goods.pop(item)
                    else:
                        self.list_goods[item]["count"] = self.list_goods[item]["count"] - count
                    print(f'{good.name} в количестве {count} единиц передано на склад {division}')


class Equipment:
    def __init__(self, name):
        self.name = name


class Printer(Equipment):
    def __init__(self, name, printing_technology, print_speed):
        super().__init__(name)
        self.printing_technology = printing_technology  # технология печати
        self.print_speed = print_speed  # скорость печати


class Scanner(Equipment):
    def __init__(self, name, scanning_speed):
        super().__init__(name)
        self.scanning_speed = scanning_speed  # скорость сканирования


class CopyMachine(Equipment):
    def __init__(self, name, copy_speed):
        super().__init__(name)
        self.copy_speed = copy_speed  # скорость копирования


printer = Printer("HP LaserJet 1018", "Лазерный", 25)
scanner = Scanner("CANON P-215II", 15)
copy_machine = CopyMachine("CANON imageRUNNER 2206N", 22)
warehouse = Warehouse()
warehouse.add_goods(printer, 5)
warehouse.add_goods(scanner, 7)
warehouse.add_goods(copy_machine, 1)
warehouse.transfer_goods(printer, 2, "Отдел кадров")
warehouse.transfer_goods(scanner, 2, "Отдел маркетига")
warehouse.transfer_goods(copy_machine, "2", "Бухгалтерия")
