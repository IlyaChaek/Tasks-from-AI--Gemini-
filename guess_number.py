'''
Текстовая игра "Угадай число"
Задача: Компьютер загадывает случайное число, а пользователь пытается его угадать. Программа должна подсказывать, больше или меньше загаданное число.
Усложнение:
    Ограничить количество попыток.
    Добавить уровни сложности (разный диапазон чисел).
    Сохранять результаты игры в файл.
'''
import random
lvl = int(input('Choose lvl of difficulty: \n1 - low;\n2 - medium;\n3 - high \n'))
if lvl == 1:
    random_number = random.randint(1,10)
elif lvl == 2:
    random_number = random.randint(1,50)
elif lvl == 3:
    random_number = random.randint(1,100)
print(random_number)
a = 10
print(f'Игра: угадай число. Тебе дается 10 попыток')
for i in range(a):
    user_number = int(input('Enter number: '))
    if user_number > random_number:
        print('Слишком большое число')
        a -= 1
        print(f'Осталось {a} попыток')
    if user_number < random_number:
        print('Слишком маленькое число')
        a -= 1
        print(f'Осталось {a} попыток')
    if user_number == random_number:
        print('Ты выиграл!')
    if a == 0:
        print('Ты проиграл. Заданное число было:', random_number)