# def count_args(*args):
#     return len(args)

# def sq_sum(*args):
#     summa = 0
#     for i in args:
#         summa += i ** 2
#     return summa


# def mean(*args):
#     count, summa = 0, 0
#     for i in args:
#         if type(i) in (int, float):
#             count += 1
#             summa += i
#
#     if count > 0:
#         return summa / count
#     else:
#         return 0.0


# def greet(name, *args):
#     if len(args) == 0:
#         stroka = 'Hello,' + name + '!'
#         return stroka
#     else:
#         stroka = 'Hello, '  + name + ' and ' + ' and '.join(args) + '!'
#         return stroka



def print_products(*args):
    count = 0
    for i in args:
        if type(i) is str and i != '':
            count += 1
            print(count, ') ', i, sep='')
    if count == 0:
        print('Нет продуктов')


print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)

