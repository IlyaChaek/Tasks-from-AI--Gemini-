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
if os.path.exists('File_data.txt'):
    file = open('File_data.txt', 'a')
else:
    file = open('File_data.txt', 'x')
start_time = time.time()
print(f'Игра: угадай число!')
lvl = int(input('Выберите уровень сложности: \n1 - Легко (число от 1 до 10, 10 попыток)\n2 - Средне (число от 1 до 50, 7 попыток)\n3 - Сложно (число от 1 до 100, 5 попыток)\n4 - Эксперт (число от 1 до 100, 3 попытки)\n5 - Нереально (число от 1 до 1.000, 5 попыток)\n6 - БЕЗУМНАЯ НЕВОЗМОЖНОСТЬ (число от 1 до 1.000, 2 попытки)\n7 - ????? (число от 1 до 1.000, 1 попытка)\n8 - Рофл режим (число от 1 до 1.000.000, 15 попыток)\n9 - Может не надо?(число от 1 до 100.000.000, 50 попыток)\nВвод: '))
if lvl == 1:
    random_number = random.randint(1,10)
    a = 10
    mode = 'Легко'
elif lvl == 2:
    random_number = random.randint(1,50)
    a = 7
    mode = 'Средне'
elif lvl == 3:
    random_number = random.randint(1,100)
    a = 5
    mode = 'Сложно'
elif lvl == 4:
    random_number = random.randint(1,100)
    a = 3
    mode = 'Эксперт'
elif lvl == 5:
    random_number = random.randint(1,1000)
    a = 5
    mode = 'Нереально'
elif lvl == 6:
    random_number = random.randint(1,1000)
    a = 2
    mode = 'БЕЗУМНАЯ НЕВОЗМОЖНОСТЬ'
elif lvl == 7:
    random_number = random.randint(1,1000)
    a = 1
    mode = '?????'
elif lvl == 8:
    random_number = random.randint(1,1000000)
    a = 15
    mode = 'Рофл режим'
elif lvl == 9:
    random_number = random.randint(1,100000000)
    a = 50
    mode = 'Может не надо?'
b = a

#!DEBUG - показ числа вначале игры ЯВЛЯЕТСЯ ЧИТОМ (рекомендуется выключить для полноты эмоций от игры)
# *DEBUG CODE START
debug_cheat = 0 #? 1 - turned on / 0 - turned off 
if debug_cheat == 1:
    print('_______________________')
    print(f'DEBUG_CHEAT:\nнеизвестное число: {random_number}')
    print('_______________________')
elif debug_cheat == 2: #hidden cheat
    print(random_number)
elif debug_cheat == 0:
    pass
# *DEBUG CODE END
start_time = time.time()
for i in range(a):
    user_number = int(input('Введите число: '))
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

last_attempts = b - a 
if debug_cheat == 2:
    file.write(f'\nДанные игры \nДата: {current_date}\nВремя:\n{current_time}\n\n\nЗагаданное число: {random_number}\nВремя отгадывания: {game_time}\nКоличество использованных попыток: {last_attempts}\nКоличество неиспользованных попыток: {a}\nРежим игры: {mode}\n')
elif debug_cheat == 1:
    file.write(f'\nДанные игры(ЧИТ ВКЛЮЧЕН) \nДата(ЧИТ ВКЛЮЧЕН): {current_date}\nВремя(ЧИТ ВКЛЮЧЕН):\n{current_time}\n\n\nЗагаданное число(ЧИТ ВКЛЮЧЕН): {random_number}\nВремя отгадывания(ЧИТ ВКЛЮЧЕН): {game_time}\nКоличество использованных попыток(ЧИТ ВКЛЮЧЕН): {last_attempts}\nКоличество неиспользованных попыток(ЧИТ ВКЛЮЧЕН): {a}\nРежим игры(ЧИТ ВКЛЮЧЕН): {mode}\n')
elif debug_cheat == 0:
    file.write(f'\nДанные игры \nДата: {current_date}\nВремя:\n{current_time}\n\n\nЗагаданное число: {random_number}\nВремя отгадывания: {game_time}\nКоличество использованных попыток: {last_attempts}\nКоличество неиспользованных попыток: {a}\nРежим игры: {mode}\n')

file.close()