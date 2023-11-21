# task045.py Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 105
# . Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).
# Ввод: Вывод:
# 300 220 284
# k = int(input("Enter number:  "))

# if k < pow(10, 5):
#     for n in range(1, k):
#         m = 0
#         sum2 = 0
#         for i in range(1, n//2+1):
#             if n % i == 0:
#                 m += i
#         for j in range(1, m//2+1):
#             if m % j == 0:
#                 sum2 += j
#         if sum2 == n and m > n:
#             print(n, m)



def sum_div(_num_):
    sum = 0
    for i in range(1, _num_ // 2 + 1):
        if _num_ % i == 0:
            sum += i
    return sum

# sum1 = sum_div(user_num)
# print(sum1)
# sum2 = sum_div(sum1)
# print(sum2)

# if user_num == sum2:
#     print('Number frendly  ')
# else:
#     print('Number enemy   ')

def main():
    user_num = 100001
    while user_num > 100000:
        user_num = int(input('Enter number:  '))
        result_list = []
        for i in range(1, user_num):
            sum1 = sum_div(i)
            sum2 = sum_div(sum1)
            sum_div(sum1)
            if i == sum2 and i!= sum1:
                if{sum1, i} in result_list:
                    continue
                result_list.append({sum1, i})
        return result_list
print(main())
