orig_list = [1,2,3,4,5]
list_copy = orig_list.copy()
print(orig_list)
print(list_copy)



orig_list_2 = [1,2,3,4,5]
copied_list_2 = [x+1 for x in orig_list_2]
print(orig_list_2)
print(copied_list_2)



original_list = [[1, 2, 3], [4, 5, 6]]
copied_list = original_list.copy()
copied_list[0][1] = 99
print("Оригинальный список:", original_list)
print("Скопированный список:", copied_list)





original_list = [1, 2, 2, 3, 4, 4, 5]

new_list = list(set(original_list))
new_list_ordered = []
for item in original_list:
    if item not in new_list_ordered:
        new_list_ordered.append(item)

print("Список без дубликатов (без сохранения порядка):", new_list)
print("Список без дубликатов (с сохранением порядка):", new_list_ordered)




list_1 = [1,2,3,4,5]
list_2 = [6,7,8,9,10]
print(list_1 + list_2)