import math
import random


def ex1():
    m = 1
    while 1.0 + 10 ** (-m) != 1.0:
        m += 1
    return m - 1


power = ex1()
u = 10 ** (-power)
print("power:", power, "u:", u)
print("\n")


def ex2():
    u = 10 ** (-power)
    x = 1.0
    y = u / 10
    z = u / 10
    sum1 = (x + y) + z
    sum2 = x + (y + z)

    print(sum1, sum2)
    print(x + y)

    print("Sum is non associative?")
    if sum1 != sum2:
        print(True)
    else:
        print(False)

    mul1 = (x * y) * z
    mul2 = x * (y * z)
    print("Multiply is non associative?")
    if mul1 != mul2:
        print(True)
    else:
        print(False)

    x = -0.1
    y = u / 10
    z = u / 10
    mul1 = (x * y) * z
    mul2 = x * (y * z)
    print("Multiply is non associative?")
    if mul1 != mul2:
        print(True)
    else:
        print(False)
    print("\n")


ex2()
