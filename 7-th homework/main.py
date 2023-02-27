from library import get_declension_coins, get_declension_hryvnia, separate_number


def print_amount():
    amount = float(input("Введіть суму: "))
    print('Надана вами сума:', (separate_number(amount)))


print_amount()