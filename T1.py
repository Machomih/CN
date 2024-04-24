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


def T(x, a):
    match x:
        case 1:
            res = a
        case 2:
            res = 3 * a / (3 - a ** 2)
        case 3:
            res = (15 * a - a ** 3) / (15 - 6 * a ** 2)
        case 4:
            res = (105 * a - 10 * a ** 3) / (105 - 45 * a ** 2 + a ** 4)
        case 5:
            res = (945 * a - 105 * a ** 3 + a ** 5) / (945 - 420 * a ** 2 + 15 * a ** 4)
        case 6:
            res = (10395 * a - 1260 * a ** 3 + 21 * a ** 5) / (10395 - 4725 * a ** 2 + 210 * a ** 4 - a ** 6)
        case 7:
            res = (135135 * a - 17325 * a ** 3 + 378 * a ** 5 - a ** 7) / (
                    135135 - 62370 * a ** 2 + 3150 * a ** 4 - 28 * a ** 6)
        case 8:
            res = (2027025 * a - 270270 * a ** 3 + 6930 * a ** 5 - 36 * a ** 7) / (
                    2027025 - 945945 * a ** 2 + 51975 * a ** 4 - 630 * a ** 6 + a ** 8)
        case 9:
            res = (34459425 * a - 4729725 * a ** 3 + 135135 * a ** 5 - 990 * a ** 7 + a ** 9) / (
                    34459425 - 16216200 * a ** 2 + 945945 * a ** 4 - 13860 * a ** 6 + 45 * a ** 8)
    return res


def ex3():
    functions = {i: 0 for i in range(4, 10)}
    for i in range(0, 10000):
        errors = []
        random_number = random.uniform(-math.pi / 2, math.pi / 2)
        val_exact = math.tan(random_number)
        for j in range(4, 10):
            errors += (j, abs(T(j, random_number) - val_exact)),
        errors.sort(key=lambda x: x[1])
        for index in range(0, 3):
            print("Function:", errors[index][0], "Error:", errors[index][1])
            functions[errors[index][0]] += 1
    for key, value in functions.items():
        print("Function:", key, "Occurrences:", value)


ex3()
