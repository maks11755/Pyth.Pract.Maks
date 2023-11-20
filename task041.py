# Задача №41. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
# Ввод: Ввод:
# 5 5
# 1 2 3 4 5 1 5 1 5 1
# Вывод: Вывод:
# 0 2
# (каждое число вводится с новой строки)

# import random

# n = int(input())
# lst = [random.randint(0, 10) for i in range(n)]
# print(lst)

# count = 0
# for i in range(1, len(lst)-1):
#     if lst[i] > lst[i-1] and lst[i] > lst[i+1]:
#         count += 1
# print(count)

list1 = [1, 2, 3, 4, 5]
list2 = [1, 5, 1, 5, 1]
def sort(list1):
    count = 0
    for i in range(1, len(list1)- 1):
        if list1[i - 1] < list1[i] and list1[i] > list1[i + 1]:
            count += 1
    return count
print(sort(list1))
print(sort(list2))    

