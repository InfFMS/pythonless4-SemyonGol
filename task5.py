# Напишите функцию, которая «переворачивает» число,
# то есть возвращает число, в котором цифры стоят в обратном порядке.
# Вводится натуральное число
# Пользоваться input()[::-1] запрещено!
# Идея задачи реализовать алгоритм,
# который будет работать для любого введенного натурального числа.
print('Enter number:', end=' ')
a = int(input())
def inv(a):
    if a < 10:
        return a
    print(a%10, end='')
    return inv(a//10)
print('Reverse number:', inv(a))