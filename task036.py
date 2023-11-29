# Задача 36:  Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.

# Ввод:                                                             Вывод:

# print_operation_table(lambda x, y: x * y)                         1         2        3        4        5       6   
#                                                                   2         4        6        8        10      12 
#                                                                   3         6        9        12       15      18 
#                                                                   4         8        12       16       20      24
#                                                                   5        10        15       20       25      30
#                                                                   6        12        18       24       30      36   

# Решение:
# n - число столбцов (элементов в строке) и строк (итераций первой строки)
# Первая строка от 1 до 6
# Вторая (2) строка - первая (1), умноженная на 2
# Третья (3) строка - первая (1), умноженная на 3
# ...
# Шестая (6) строка - первая (1), умноженная на 6


# def print_operation_table(operation, n, m):
#     table = []
#     for i in range(1, n + 1):
#         line = []
#         for j in range(1, m + 1):
#             line.append(operation(i, j))
#         table.append(line)

#     for row in table:
#         print(("{: <7}"*m).format(*row))

#     print("Искомый элемент> ", operation(n,m))

# x, y = map(int, input("Введите 2 значения через пробел> ").split())
# print_operation_table(lambda x, y: x * y, x, y)


def print_operation_table(operation, num_rows, num_columns):
    if num_rows < 2:
        print('Error. Enter number > 2')
    else:
        for i in range(1, num_rows + 1):
            if i == 1:
                sq = [i for i in range(1, num_rows + 1)]
            else:
                sq = [operation(i, j) if j > 1 else i for j in range(1, num_columns + 1)]
            print(*sq)


print_operation_table(lambda x, y: x + y, 8, 8)