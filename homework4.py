# a = [int(x) for x in input().split()]
# b = [int(i) for i in input().split()]
# set1 = set(a)
# set2 = set(b)
# print(set1)
# print(set2)
# massive = list(set1 & set2)
# massive.sort()
# for i in massive:
#     print(i, end=' ')



from random import randint
list_1 = list(randint(1, 5) for i in range(int(input('Введите кол-во кустов: '))))
print(list_1)
a = int(input('Введите № куста: '))
res = 0
if a == 1:
   res = list_1[0] + list_1[1] + list_1[-1]
elif a == len(list_1):
    res = list_1[-2] + list_1[-1] + list_1[0]
else:
    res = list_1[a-1] + list_1[a-2] + list_1[a]
print(res, 'ягод')