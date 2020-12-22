"""Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц,
год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных."""


class Data:
    str_date = None

    def __init__(self, str_date):
        self.str_date = str_date
        Data.str_date = str_date

    @staticmethod
    def validation_date(list_date):
        list_month = {"1": 31, "2": 28, "3": 31, "4": 30, "5": 31, "6": 30, "7": 31, "8": 31, "9": 30, "10": 31,\
        "11": 30, "12": 31}
        for index in range(len(list_date)-1):
            if index == 0:
                if list_date[0] > list_month[str(list_date[1])] or list_date[0] <= 0:
                    return f'Дата не прошла валидацию'
            elif index == 1:
                if list_date[1] > 12 or list_date[1] <= 0:
                    return f'Дата не прошла валидацию'
            else:
                if list_date[2] > 3000 or list_date[2] <= 0:
                    return f'Дата не прошла валидацию'
            return f'Дата прошла валидацию!!!'

    @classmethod
    def date_int(cls):
        new_list_date = list()
        str_date = cls.str_date
        list_date = str_date.split("-")
        for item in list_date:
            new_list_date.append(int(item))
        return Data.validation_date(new_list_date)


date = Data("31-12-2020")
print(date.date_int())
date1 = Data("32-12-2020")
print(date1.date_int())
