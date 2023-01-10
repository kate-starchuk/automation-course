
'''Є list довільних чисел, наприклад [11, 77, 4, 22, 0, 56, 5, 95, 7, 5, 87, 13, 45, 67, 44].
 Напишіть код, який видалить (не створить новий, а саме видалить!) з нього всі числа, які менше 21 і більше 74.'''

lst = [11, 77, 4, 22, 0, 56, 5, 95, 7, 5, 87, 13, 45, 67, 44]
for i in lst.copy():
    if i > 74 or i < 21:
        lst.remove(i)
print(lst)


'''Є два довільних числа які відповідають за мінімальну і максимальну ціну. Є Dict з назвами магазинів і цінами:
{ "cito": 47.999, "BB_studio" 42.999, "momo": 49.999, "main-service": 37.245, "buy.now": 38.324, "x-store": 37.166,
"the_partner": 38.988, "store": 37.720, "rozetka": 38.003}. Напишіть код, який знайде і виведе на екран назви 
магазинів, ціни яких попадають в діапазон між мінімальною і максимальною ціною.'''
dct = {
    "cito": 47.999,
    "BB_studio": 42.999,
    "momo": 49.999,
    "main-service": 37.245,
    "buy.now": 38.324,
    "x-store": 37.166,
    "the_partner": 38.988,
    "store": 37.720,
    "rozetka": 38.003
}
lower_limit = 0
upper_limit = 0
while True:
    try:
        lower_limit = float(input('Мінімальна вартість: '))
    except ValueError:
        print("Будь ласка, введіть число")
        continue
    else:
        break

while True:
    try:
        upper_limit = float(input('Максимальна вартість: '))
    except ValueError:
        print("Будь ласка, введіть число")
        continue
    else:
        break

shops = []
for item in dct.items():
    if lower_limit <= item[1] <= upper_limit:
        shops.append(item[0])
print('Магазини: ', shops)
























