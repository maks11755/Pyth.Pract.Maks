# task043. Решение в группах
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод:   Вывод:
# 1 2 3 2 3   2

# count = 0
# lst = list(map(int, input().split()))
# print(lst)
# for i in range(len(lst)):
#     for j in range(i+1,len(lst)):
#         if lst[i] == lst[j]:
#             count += 1
# print(count)

import random 

def create_random_list(num):
    return [random.randint(0, 10) for _ in range(num )]

def find_couple(_user_list_: list):
    count_of_couple = 0
    for i in set(_user_list_):
        count_of_couple += _user_list_.count(i) // 2
    return count_of_couple

len_list = int(input('Enter length array:  '))
user_array = create_random_list(len_list)

print(user_array)
print(find_couple(user_array))
# find_couple(user_array)
# print(find_couple(user_array))
# print(create_random_list(len_list))
# print(find_couple(create_random_list(len_list)))