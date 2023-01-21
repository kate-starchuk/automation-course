"""
Напишіть программу "Касир в кінотеатрі", яка буде виконувати наступне:
Попросіть користувача ввести свсвій вік.
- якщо користувачу менше 7 - вивести "Тобі ж <>! Де твої батьки?"

- якщо користувачу менше 16 - вивести "Тобі лише <>, а це е фільм для дорослих!"

- якщо користувачу більше 65 - вивести "Вам <>? Покажіть пенсійне посвідчення!"

- якщо вік користувача складається з однакових цифр (11, 22, 44 і тд років, всі можливі варіанти!) - вивести "О, вам <>!
 Який цікавий вік!"

- у будь-якому іншому випадку - вивести "Незважаючи на те, що вам <>, білетів всеодно нема!"

Замість <> в кожну відповідь підставте значення віку (цифру) та правильну форму слова рік
Для будь-якої відповіді форма слова "рік" має відповідати значенню віку користувача.
Після отримання відповіді програма повинна спитати користувача, чи хоче він повторити виконання.
Користувач відповідає Yes або No. У випадку коли користувач відповів Yes програма повторюється, No - завершується.
Користувач повинен мати змогу повторити виконання програми необмежену кількість разів.
"""


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


cashier_in_cinema()



























