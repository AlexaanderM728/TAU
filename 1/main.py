from math import pi


def funkcja_silni(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * funkcja_silni(n - 1)


def circle_area(r):
    return pi * (r ** 2)


def same_number(a, b):

    if a or b == chr():
        print("input int")
        return None
    if a == b:
        return True
    else:
        return False


a = int(2)
b = int(2)
print(same_number(a, b))
