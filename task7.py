# Напишите функцию is_valid_triangle(side1, side2, side3),
# которая принимает в качестве аргументов три натуральных числа,
# и возвращает значение True, если существует невырожденный треугольник
# со сторонами side1, side2, side3, или False в противном случае.
print('Enter sides of triangle:')
side1 = int(input())
side2 = int(input())
side3 = int(input())
def is_valid_triangle(side1, side2, side3):
    if side1 < side2 + side3 and side2 < side1 + side3 and side3 < side1 + side2:
        return True
    else:
        return side1, side2, side3
print(is_valid_triangle(side1, side2, side3))
