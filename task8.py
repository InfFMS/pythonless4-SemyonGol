# Напишите рекурсивную функцию, которая
# раскладывает натуральное число на простые сомножители.
# Пример:
# Ввод:
# 378
# Вывод:
# 2*3*3*3*7
def prime(x):
    for i in range(2, x):
        if x%i == 0:
            return False
    return True
a = int(input())
def fact(a):
    if prime(a):
        return a
    for i in range(2, a):
        if (a % i == 0) and prime(i):
            print(i, '*', end='', sep='')
            return fact(a//i)
print(fact(a))