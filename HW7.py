# Написати рекурсивну функцію знаходження ступеня числа.


def power(number, power_for_nr):

    if power_for_nr == 0:
        return 1
    else:
        return number * power(number, power_for_nr - 1)
number = int(input("Это число:"))
power_for_nr = int(input("В степени:"))
result = power(number, power_for_nr)
print(result)

