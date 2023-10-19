#task 003. В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32
a = int(input('enter the number of the student in class 1'))
b = int(input('enter the number of the student in class 2'))
c = int(input('enter the number of the student in class 3'))
d = (round((a+b+c) / 2) )
print(d) 

