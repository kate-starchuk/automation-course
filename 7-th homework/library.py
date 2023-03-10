
def get_declension_kopiyka(arg: str) -> str:
    if 11 <= int(arg) <= 19:
        return 'копійок'
    elif arg[-1] == '1':
        return 'копійка'
    elif arg[-1] == '2' or arg[-1] == '3' or arg[-1] == '4':
        return 'копійки'
    else:
        return 'копійок'


def get_declension_hryvnia(arg: str) -> str:
    if 11 <= int(arg) <= 19:
        return 'гривень'
    elif arg[-1] == '1':
        return 'гривня'
    elif arg[-1] == '2' or arg[-1] == '3' or arg[-1] == '4':
        return 'гривні'
    else:
        return 'гривень'


def separate_number(num: float) -> str:
    """
    this function separates decimal part from whole part of the number
    Args:
        num: float

    Returns: separated decimal part and whole part of the number with corresponding declension

    """
    rounded_num = round(num, 2)
    whole_part = str(int(num))
    fraction_part = str(rounded_num).split(".")[1]
    return ' '.join([whole_part, get_declension_hryvnia(whole_part), fraction_part, get_declension_kopiyka(fraction_part)])


def is_hot_today(temperature: int = 30) -> bool:
    return temperature >= 25


def get_valid_number(message="Введіть число") -> float:
    """
    this function is basically a cycle for getting expected input from a user

    """
    while True:
        try:
            number = float(input(message))
            return number
        except ValueError:
            print("Будь ласка, введіть число.")
