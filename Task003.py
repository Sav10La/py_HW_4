# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

l = []

def input_list(l):
    n = int(input("Введите количество элементов: "))
    for i in range(0, n):
        e = int(input('Введите элементы: '))
        l.append(e)
    return l

def non_repeated_els(l):
    return [i for i in l if l.count(i) == 1]

print(non_repeated_els(input_list(l)))

# a = [int(i) for i in input('Enter numbers: ').split()]

# for i in a:
#     if a.count(i) == 1:
#         print(i)