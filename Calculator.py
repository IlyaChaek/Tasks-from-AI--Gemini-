'''
# *Написать программу, которая принимает два числа и математический оператор (+, -, *, /) от пользователя в консоли и выводит результат операции. 
Усложнение:
# *Добавить проверку на деление на ноль.
# *Реализовать поддержку дополнительных операций (например, возведение в степень, модульное деление).
#todo Создать меню для выбора операции.
'''
class Calculator:
    def sum(a, b):
        return a + b
    def minus(a, b):
        return a - b
    def division(a, b):
        if b == 0:
            print('Деление не возможно')
        else: 
            return a / b
    def stepen(a):
        return a*a
    def modul_division(a,b):
        return a % b
    
    def multiplication(a, b):
        return a * b
