'''
Задача: написать код, который будет создавать и удалять задачи в списке задач.
Усложнение: запись должна производиться в файл.
'''

file = open('Tasks_manager_file.txt', 'a')

def add_task(task):
    file.write(f'\n{task}\n')
    file.close
def remove_tasks():
    i = input('Вы действительно хотите очистить спиок задач? y (Yes/Да) или n (No/Нет)\nВвод: ')
    if i == 'y':
        file = open('Tasks_manager_file.txt', 'w')
        file.write(' ')
        file.close()
        print('Задачи успешно удалены!')
    elif i == 'n':
        print('Отмена удаления списка задач')
    else:
        print('Некорректный ввод. Выберите y(Yes/Да) или n(No/Нет)')
# Examples

# add_task('Название задачи') / Добавление задачи
# remove_tasks() / Удаление задач