def print_stars(quantity):

    if quantity == 0:
        return

    print('*', end='')
    print_stars(quantity - 1)


quantity = int(input("Введите число:" ))
print_stars(quantity)
