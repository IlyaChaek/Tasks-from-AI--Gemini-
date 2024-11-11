my_list = []
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)
my_list.remove(1)
print(my_list)

my_list2 = [4, 5, 1, 3, 2]
my_list2.sort() #Сортировка по возрастанию
print(my_list2)

my_list3 = [3, 1, 2, 52, 228]
print(my_list3[:3])#Вывод первых трех элементов




my_list_4 = [1,2,3,4,5,1,1] #Создание списка
s = my_list_4.count(1) #Подсчет количества элементов списка
print(s) #Вывод количества


my_list_5 = [1, 2, 4, 5, 6] 
my_list_6 = []
my_list_6.extend(my_list_5)
print(my_list_6)

my_list_6.reverse() 
print(my_list_6)




list_with_dublicate = ['haski', 'brusko', 'podonki', 'iceberg','haski','haski','brusko','brusko','podonki', 'iceberg']
list_without_dublicate=[] #Создание списка без дубликатов
for i in list_with_dublicate: 
    if i not in list_without_dublicate: #Проверка на наличие дубликатов
        list_without_dublicate.append(i) #Добавление в список без дубликатов
print(list_without_dublicate) #Вывод списка без дубликатов
