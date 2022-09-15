# 1. Вычислить число π c заданной точностью d
# *Пример:* 
# - при d = 0.001, π = 3.141.$    10^{-1} ≤ d ≤10^{-10}

# ряд Лейбница
# 4 * pi = Sum of k ∈ [1; ∞) { (-1) ^ (k+1) / (2k-1) }
# pi = 4 * (1 - 1/3 + 1/5 - 1/7 + 1/9 - ...)
# pi = 4 - 4/3 + 4/5 - 4/7 + 4/9 - ...

d = input('Введите точность: ')

def precise_pi(d):
    k = 1
    sum = 0
    for i in range(1000000):
        # even index elements are positive
        if i % 2 == 0:
            sum += 4 / k
        else:
            # odd index elements are negative
            sum -= 4 / k
        # denominator is odd
        k += 2
    return sum

def count_decimals(number):
    count = len(str(number).split(".")[1])
    return count

decimals = count_decimals(d)
print(round(precise_pi(d),decimals))