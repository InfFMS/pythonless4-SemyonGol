# Напишите функцию number_to_words(num), которая принимает
# в качестве аргумента натуральное число num и возвращает
# его словесное описание на русском языке.
#
# Примечание 1.
# Считайте, что число 1 ≤ num ≤ 99.
#
# Примечание 2.
# Следующий программный код:
#
# print(number_to_words(7))
# print(number_to_words(85))
# должен выводить:
#
# семь
# восемьдесят пять
num = input()
def num_(num):
    if num[-1] == '1':
        b = 'один'
    elif num[-1] == '2':
        b = 'два'
    elif num[-1] == '3':
        b = "три"
    elif num[-1] == '4':
        b = 'четыре'
    elif num[-1] == '5':
        b = 'пять'
    elif num[-1] == '6':
        b = 'шесть'
    elif num[-1] == '7':
        b = 'семь'
    elif num[-1] == '8':
        b = 'восемь'
    elif num[-1] == '9':
        b = 'девять'
    elif num[-1] == '0':
        b = ''
    num = int(num)
    if num < 10:
        print(b)
    if  num > 19:
        num = str(num)
        if num[-2] == '2':
            a = 'Двадцать'
        elif num[-2] == '3':
            a = "Тридцать"
        elif num[-2] == '4':
            a = 'Сорок'
        elif num[-2] == '5':
            a = 'Пятьдесят'
        elif num[-2] == '6':
            a = 'Шестьдесят'
        elif num[-2] == '7':
            a = 'Семьдесят'
        elif num[-2] == '8':
            a = 'Восемьдесят'
        elif num[-2] == '9':
            a = 'Девяносто'
        print(a, b)
    num = int(num)
    if 19 > num > 9:
        num = str(num)
        if num[-1] == '1':
            b = 'Одинадцать'
        elif num[-1] == '2':
            b = 'Двенадцать'
        elif num[-1] == '3':
            b = "Тринадцать"
        elif num[-1] == '4':
            b = 'Четырнадцать'
        elif num[-1] == '5':
            b = 'Пятнадцать'
        elif num[-1] == '6':
            b = 'Шестнадцать'
        elif num[-1] == '7':
            b = 'Семнадцать'
        elif num[-1] == '8':
            b = 'Восемнадцать'
        elif num[-1] == '9':
            b = 'Девятьнадцать'
        elif num[-1] == '0':
            b = 'Десять'
        print(b)
    return ''
print(num_(num))