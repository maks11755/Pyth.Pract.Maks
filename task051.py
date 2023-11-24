# task051. Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.
# Ввод: Вывод:
# values = [0, 2, 10, 6] same
# if same_by(lambda x: x % 2, values):
# print(‘same’)
# else:
# print(‘different’)

"""values = [3, 5, 1]
if same_by(lambda x: True if x % 2 == 1 else False, values):
    print('same')
else:
    print('different')"""

# values = [0, 2, 10, 6]
# same_by = list(filter(lambda a: True if a % 2 == 0 else False, values))
# if len(values) == len(same_by):
#     print('same')
# else:
#     print('different')

values = [0, 2, 4, 6, 1]
def same_by(charactersistic, objects):
    for i in objects:
    
        if charactersistic(i) != True:
            return False
    return True

if same_by(lambda x : x >= 0, values):
    print('same')
else:
    print('different')