# n = int(input("Введите целое неотрицательное число: "))
# res = 1
# i = 1
#
# while i <= n:
#     res *= i
#     i += 1
# print(res)

# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.


# a1 = 0
# a2 = 1
# count = 2
# target = int(input())
# while target > a2:
#       a2 = a1 + a2
#       a1 = a2 - a1
#       count = count +  1
# if target == a2:
#    print(count)
# else:
#    print(-1)

# Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

n = int(input('Введите N: '))
min = float('inf')
max = 0
for i in range(n):
    a = int(input())
    if a < min:
        min = a
    if a > max:
        max = a
print(f'{min}{max}')

