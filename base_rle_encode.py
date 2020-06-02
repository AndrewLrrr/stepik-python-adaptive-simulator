"""
Кодирование длин серий — это базовый алгоритм сжатия данных.

В этой задаче мы реализуем одну из самых простых его вариантов.

На вход алгоритму подаётся строка, содержащая символы латинского алфавита.
Эта строка разбивается на группы одинаковых символов, идущих подряд ("серии").
Каждая серия характеризуется повторяющимся символом и количеством повторений.
Именно эта информация и записывается в код: сначала пишется длина серии повторяющихся символов,
затем сам символ. У серий длиной в один символ количество повторений будем опускать.

Например, рассмотрим строку

aaabccccCCaB

Разобъём её на серии
aaa b cccc CC a B

После чего закодируем серии и получим итоговую строку, которую и будем считать результатом работы алгоритма.
3ab4c2CaB

Формат ввода:
Одна строка, содержащая произвольные символы латинского алфавита.

Формат вывода:
Строка, содержащая закодированную последовательность.
"""


from itertools import groupby


def encode_rle_short(string):
    group = [(k, len(list(g))) for k, g in groupby(string)]
    return ''.join([str(c) + l if c > 1 else l for l, c in group])


def encode_rle_long(string):
    try:
        prev = string[0]
    except IndexError:
        return string

    count = 0
    res = ''

    for char in string:
        if char != prev:
            res += str(count) + prev if count > 1 else prev
            prev = char
            count = 1
        else:
            count += 1
    return res + (str(count) + prev if count > 1 else prev)


if __name__ == '__main__':
    print(encode_rle_long(input()))
