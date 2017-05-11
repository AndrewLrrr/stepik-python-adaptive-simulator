"""
Напишите функцию modify_list(l), которая принимает на вход список целых чисел, удаляет из него все нечётные значения,
а чётные нацело делит на два. Функция не должна ничего возвращать, требуется только изменение переданного списка,
например:

lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))  # None
print(lst)               # [1, 2, 3]
modify_list(lst)
print(lst)               # [1]

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)               # [5, 4]
Также функция не должна осуществлять ввод/вывод информации.
"""


def modify_list(l):
    l[:] = [x // 2 for x in l if x % 2 == 0]


# def modify_list(l):
#     def get_next():
#         for x in l:
#             if x % 2 == 0:
#                 yield x // 2
#     l[:] = get_next()


# def modify_list(l):
#     for item in l[::]:
#         if item % 2 != 0:
#             l.remove(item)
#     for idx, item in enumerate(l):
#         l[idx] //= 2

