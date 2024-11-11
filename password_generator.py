'''
Написать программу, которая генерирует случайные пароли заданной длины,
включающие буквы (заглавные и строчные), цифры и специальные символы.
Усложнение:

#TODO  Позволить пользователю задавать количество символов каждого типа.
    Создать функцию для проверки надежности сгенерированного пароля.
'''

import string
import random

def generate_password(lenght):
    random_pass = string.ascii_letters + string.digits  + string.punctuation
    password = ''.join(random.choice(random_pass) for i in range(lenght))
    return password
generated_password = generate_password(8)
print(generated_password)
def check_password(generated_password):
    if len(generated_password) > 8:
        print('Password is security')
    else:
        print('Password is low-security. Please add simbols in password')
check_password(generated_password)