"""
Напишіть декоратор, який вимірює і виводить на екран час виконання функції в секундах
і задекоруйте ним основну функцію гри з попередньої дз. Після закінчення гри декоратор
має сповістити, скільки тривала гра.
Винесіть всі функції та декоратор в окремий файл та виконайте імпорт в основний
"""

from functools import wraps
import time


def timeit(func):
    # @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds')
        return result
    return timeit_wrapper


def get_declension(arg_age):
    """
    Declination of the word 'вік' for message
    Args:
        arg_age:

    Returns:

    """

    if 11 <= int(arg_age) <= 19:
        return 'років'
    elif arg_age[-1] == '1':
        return 'рік'
    elif arg_age[-1] == '2' or arg_age[-1] == '3' or arg_age[-1] == '4':
        return 'роки'
    else:
        return 'років'


@timeit
def cashier_in_cinema():
    print('\"Касир в кінотеатрі\"')
    while True:
        try:
            age = int(input('Введіть свій вік в роках '))

            if age < 7:
                print("Тобі ж", age, get_declension(str(age)), "! Де твої батьки?")
            elif (age % 11) == 0:
                print('О, вам', age, get_declension(str(age)), '! Який цікавий вік!')
            elif age < 16:
                print("Тобі ж", age, get_declension(str(age)), ", а це е фільм для дорослих!")
            elif age > 65:
                print('Вам', age, get_declension(str(age)), '?', 'Покажіть пенсійне посвідчення!')
            else:
                print('Незважаючи на те, що вам', age, get_declension(str(age)), 'білетів всеодно нема!')
        except ValueError:
            print('Ввід не правильний.')
        try_again = ""
        while try_again not in ["yes", "no"]:
            try_again = input("Введіть Yes щоб спробувати знову або No, щоб закінчити ").lower()
            if try_again in ["yes", "no"]:
                continue
            else:
                print("Неправильний ввід. Введіть Yes щоб спробувати знову або No, щоб закінчити")
        if try_again == "no":
            break

