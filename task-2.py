"""Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
ситуацию и не завершиться с ошибкой."""


class ErrorByZero(Exception):
    def __init__(self, text_error):
        self.text_error = text_error

    def __str__(self):
        return self.text_error


try:
    number1 = int(input("Введите чеслитедь: "))
    number2 = int(input("Введите знаменатель: "))
    if number2 == 0:
        raise ErrorByZero("Деление на ноль запрещено!")
except ValueError as ve:
    print("Вы ввели не число!")
except ErrorByZero as err:
    print(err)
else:
    result = number1 / number2
    print(result)
