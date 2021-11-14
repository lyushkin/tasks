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


def greet(*args):
    if len(args) < 1:
        return (f"Hello{args}!")
    else:
        return ('Hello, ', *args)

print(greet('Timur'))
print(greet('Timur', 'Roman'))
print(greet('Timur', 'Roman', 'Ruslan'))