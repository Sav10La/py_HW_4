# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# *Пример:* 
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import*


print()
k = int(input("Введите число: "))
polynomial = list()
print()

if k == 0: print(f"При степени k = {k} невозможно сождать многочлен")

else:
    while k >= 0:
        num = randint(0, 101)
        if num == 0:
            k -= 1
            continue
        elif num == 1:
            if k == 0: polynomial.append(str(num))
            elif k == 1: polynomial.append("x")
            else: polynomial.append("x^" + str(k))
        else:
            if k == 0: polynomial.append(str(num))
            elif k == 1: polynomial.append(str(num) + "x")
            else: polynomial.append(str(num) + "x^" + str(k))
        k -= 1

s = " + ".join(polynomial) + " = 0"
print(s)

with open('polynomial.txt', 'w') as file:
    file.writelines(s)
    file.close()