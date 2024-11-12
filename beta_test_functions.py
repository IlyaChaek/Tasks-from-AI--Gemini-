import datetime
current_date = datetime.datetime.now().strftime('\n%Y-%m-%d')
current_time = datetime.datetime.now().strftime('%X')
print(f'\nДата:{current_date}\nВремя:\n{current_time}')
