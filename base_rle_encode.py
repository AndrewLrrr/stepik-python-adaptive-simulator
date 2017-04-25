# Кодирование длин серий — это базовый алгоритм сжатия данных.
#
# В этой задаче мы реализуем одну из самых простых его вариантов.
#
# На вход алгоритму подаётся строка, содержащая символы латинского алфавита.
# Эта строка разбивается на группы одинаковых символов, идущих подряд ("серии").
# Каждая серия характеризуется повторяющимся символом и количеством повторений.
# Именно эта информация и записывается в код: сначала пишется длина серии повторяющихся символов,
# затем сам символ. У серий длиной в один символ количество повторений будем опускать.
#
# Например, рассмотрим строку
#
# aaabccccCCaB
#
# Разобъём её на серии
# aaa b cccc CC a B
#
# После чего закодируем серии и получим итоговую строку, которую и будем считать результатом работы алгоритма.
# 3ab4c2CaB
#
# Формат ввода:
# Одна строка, содержащая произвольные символы латинского алфавита.
#
# Формат вывода:
# Строка, содержащая закодированную последовательность.
#
# from itertools import groupby
#
# def encode_rle_short(string):
#     group = [list(g) for k, g in groupby(string)]
#     print(group)
#     return ''.join([char[0] for char in group])


def compress_sequence(string, char, length):
    return string.replace(char * length, str(length) + char, 1)


def encode_rle(string):
    if not string:
        return string

    chars = list(string)
    current_char = ''
    char_counter = 1

    for char in chars:
        if not current_char:
            current_char = char
        else:
            if current_char == char:
                char_counter += 1
            else:
                if char_counter > 1:
                    string = compress_sequence(string, current_char, char_counter)
                char_counter = 1
                current_char = char

    if char_counter > 1:
        string = compress_sequence(string, current_char, char_counter)

    return string


def main():
    print(encode_rle(input()))


if __name__ == '__main__':
    main()

