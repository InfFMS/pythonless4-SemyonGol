# Напишите функцию, которая сокращает дробь вида M/N.
# Где M и N - наутральные числа.
# В качестве аргументов она принимает числитель и знаменатель,
# выводит числитель и знаменатель после сокращения
#
# Пример:
# Ввод:
# 25 15
# Вывод:
# 5 3
def gcd(a, b, p = 1):
    if a == b:
        return a
    elif a%b == 0 or b%a == 0:
        return min(a, b)
    for i in range(2, min(a, b)):
        if a%i == 0 and b%i == 0:
            p = i
    return p
print('Enter numerator of fraction:', end=' ')
n = int(input())
print('Enter denominator of fraction:', end=' ')
d = int(input())
def frdiv(n, d):
    if n == d:
        return 1
    if gcd(n, d) == 1:
        return n, d
    else:
        c = gcd(n, d)
        n = n/c
        d = d/c
        return n, d
a1, a2 = frdiv(n, d)
print(f"{a1:.0f}/{a2:.0f}")