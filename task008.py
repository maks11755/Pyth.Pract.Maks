# Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no
# n,m,k = int(input('В-те 1-ю сторону: ')),int(input('В-те 2-ю сторону: ')),int(input('В-те кол-во долек: '))
# if k%n == 0 or k%m == 0:
#     print('Yes')
# else: print('No')
# или
# if k < n*m and (k % n == 0 or k % m == 0)
n = int(input('Enter n   '  ))
m = int(input('Enter m   '  ))
k = int(input('Enter the number of slices k   '))
s = m * n
if((s / k == m)  or (s / k == n)): 
  print('Yes')
else: print('No')