'''
Текстовая игра "Угадай число"
Задача: Компьютер загадывает случайное число, а пользователь пытается его угадать. Программа должна подсказывать, больше или меньше загаданное число.
Усложнение:
    Ограничить количество попыток.
    Добавить уровни сложности (разный диапазон чисел).
    Сохранять результаты игры в файл.
'''
import time
import random
import os.path
import datetime
current_date = datetime.datetime.now().strftime('\n%Y-%m-%d')
current_time = datetime.datetime.now().strftime('%X')
print(f'\nДата:{current_date}\nВремя:\n{current_time}')

if os.path.exists('File_data.txt'):
    file = open('File_data.txt', 'a')
else:
    file = open('File_data.txt', 'x')
start_time = time.time()
print(f'Игра: угадай число. Тебе дается 10 попыток')
lvl = int(input('Choose lvl of difficulty: \n1 - low;\n2 - medium;\n3 - high \nEnter: '))
if lvl == 1:
    random_number = random.randint(1,10)
elif lvl == 2:
    random_number = random.randint(1,50)
elif lvl == 3:
    random_number = random.randint(1,100)
print(f'Debug:\nrandom_number = {random_number}')
a = 10
start_time = time.time()
for i in range(a):
    user_number = int(input('Enter number: '))
    if user_number > random_number:
        print('Слишком большое число')
        a -= 1
        print(f'Осталось {a} попыток')
    elif user_number < random_number:
        print('Слишком маленькое число')
        a -= 1
        print(f'Осталось {a} попыток')
    elif user_number == random_number:
        print('Ты выиграл!')
        end_time = time.time() 
        break
    elif a == 0:
        print('Ты проиграл. Заданное число было:', random_number)
        end_time = time.time()     
        break
game_time_not_formatted = end_time - start_time
game_time = round(game_time_not_formatted, 2)
print(f'Время игры: {game_time} секунд')
last_attempts = 10 - a
file.write(f'\nДанные игры \nДата{current_date}\nВремя{current_time}:\nЗагаданное число: {random_number};\nВремя отгадывания: {game_time}\nКоличество использованных попыток: {last_attempts}\nКоличество неиспользованных попыток: {a}')
file.close()