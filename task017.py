# task017.Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
# m = 555
# m = str(m)
# sum_digits = 0
# for j in m:
#     sum_digits += int(j)
# print(sum_digits)
# def digits_sum(m):
#     m = str(m)
#     sum_digits = 0
#     for j in m:
#         sum_digits += int(j)
#     return sum_digits
# print(digits_sum(345))
# list_num = [1, 1, 2, 0, -1, 3, 4, 4]
# print(len(set(list_num)))
# print(set(list_num))

from random import randint
list = []
count = 0
for i in range(25):
    list.append(randint(1,100))
print(list)
for i in list:
    if list[1] != list:
        count += 2
print("a have", count, "different number")

