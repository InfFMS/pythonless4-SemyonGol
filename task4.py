# Напишите функцию, которая находит
# наибольший общий делитель двух натуральных чисел
# На входе два числа, на выходе их НОД.
print('Enter two numbers:')
a = int(input())
b = int(input())
def gcd(a, b, p = 1):
    if a == b:
        return a
    elif a%b == 0 or b%a == 0:
        return min(a, b)
    for i in range(2, min(a, b)):
        if a%i == 0 and b%i == 0:
            p = i
    return p
print('GCD of your numbers:', gcd(a, b))