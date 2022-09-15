# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input('Введите число: '))

def prime_factors(n):
    fact = []
    while n % 2 == 0:
        fact.append(2)
        n = n / 2
    for i in range(3, int(n**(1/2)) + 1, 2):
        while n % i == 0:
            fact.append(i)
            n = n / i
    if n > 2:
        fact.append(int(n))
    return fact
         
print(prime_factors(n))