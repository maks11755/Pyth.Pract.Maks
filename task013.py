# Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая длинная оттепель за всю историю наблюдений за погодой.
# Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики за прошлые годы. Их интересует, сколько дней длилась самая длинная оттепель.
# Оттепелью они называют период, в который среднесуточная температура ежедневно превышала 0 градусов Цельсия. Напишите программу, помогающую синоптикам в работе.
# Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках располагается N целых чисел.
# Каждое число – среднесуточная температура в соответствующий день. Температуры – целые числа и лежат в диапазоне от –50 до 50
# Input:    6 -> -20 30 -40 50 10 -10
# Output: 2
# for

n = int(input("N = "))
stemp = 0
s = 0
for i in range(n):
    check = 1
    while check == 1:
        print("Input temp of day", i+1, " = (-50, 50)")
        d = int(input())
        if -51 < d < 51:
            check = 0
    if d >= 0:
        s += 1
        if s > stemp:
            stemp = s
    else:
        if s > stemp:
            stemp = s
        s = 0
print("Days whits positive temp ->", stemp)