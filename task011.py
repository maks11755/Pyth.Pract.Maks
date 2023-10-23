#task011. Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1
# n = int(input("A = "))
# a1 = 1
# a2 = 1
# a = 1
# i = 3
# if n == 0:
#     print("i = 1")
# elif n == 1:
#     print("i = 2, 3")
# elif n < 0:
#     print("Error input")
# else:
#     while a < n:
#         i += 1
#         a = a1+a2
#         a1 = a2
#         a2 = a
#     if n == a:
#         print("i =", i)
#     else:
#         print("-1")

n = int(input("Enter number "))
a = 1
b = 0
i = 1
fibonacci = 0
count = 0

while i <= n + 1:
# print(fibonacci, end=" ")
    if fibonacci == n:
# print(f"\nЧисло {n} по счету на {i} месте")
        break
    fibonacci = a + b
    a = b
    b = fibonacci
    i += 1
else:
    i = -1
print(i)