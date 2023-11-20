# task039.Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод: Вывод:
# 7 3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1 (каждое число вводится с новой строки)

# import random
# n = int(input())
# lst1=[random.randint(0,10) for i in range(n)]
# print(lst1)

# m = int(input())
# lst2=[random.randint(0,10) for i in range(m)]
# print(lst2)

# lst3=[]
# for i in lst1:
#     if i not in lst2:
#         lst3.append(i)

# print(lst3) 


import random
def filter_list(array1, array2):
    res_array = []
    for i in array1:
        if i not in array2:
            res_array.append(i)
    return res_array

def create_random_list(number):
    return [random.randint(-10, 10) for _ in range(number+1)]
    
number_1 = int(input("Enter number first array =  "))
int_array_1 = create_random_list(number_1)
print(int_array_1)
number_2 = int(input("Enter number second array =  "))
int_array_2 = create_random_list(number_2)
print(int_array_2)
print(filter_list(int_array_1, int_array_2))
# interList = [i for i in firstArray if i in set(firstArray) - set(secondArray)]



