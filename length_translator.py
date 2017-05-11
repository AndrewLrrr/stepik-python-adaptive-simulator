"""
Требуется написать программу, осуществляющую преобразование из одних единиц измерения длины в другие.

Должны поддерживаться

 мили (1 mile = 1609 m),
ярды (1 yard = 0.9144 m),
футы (1 foot = 30.48 cm),
дюймы (1 inch = 2.54 cm),
километры (1 km = 1000 m),
метры (m),
сантиметры (1 cm = 0.01 m)
миллиметры (1 mm = 0.001 m)
Используйте именно указанные в формулировке задачи единицы измерения с указанной точностью.

Формат ввода:
Одна строка с фразой следующего вида:
<number> <unit_from> in <unit_to>
например, если пришла фраза "15.5 mile in km", то требуется перевести 15.5 миль в километры.

Формат вывода:
Дробное число в научном формате (экспоненциальном), с точностью ровно два знака после запятой.
"""


def from_mm(length, unit):
    unit_to_multiplier = {
        'mm': 1,
        'cm': 10 ** -1,
        'm': 10 ** -3,
        'inch': (10 ** -1) / 2.54,
        'foot': (10 ** -1) / 30.48,
        'yard': (10 ** -3) / 0.9144,
        'km': 10 ** -6,
        'mile': (10 ** -6) / 1.609,
    }

    if unit not in unit_to_multiplier:
        raise IndexError

    return length * unit_to_multiplier[unit]


def to_mm(length, unit):
    unit_to_multiplier = {
        'mm': 1,
        'cm': 10,
        'm': 10 ** 3,
        'inch': 2.54 * 10,
        'foot': 30.48 * 10,
        'yard': (10 ** 3) * 0.9144,
        'km': 10 ** 6,
        'mile': 1.609 * (10 ** 6)
    }

    if unit not in unit_to_multiplier:
        raise IndexError

    return length * unit_to_multiplier[unit]


def translator(length, from_unit, to_unit):
    length = from_mm(to_mm(length, from_unit), to_unit)

    return '{:.2e}'.format(length)


def main():
    length, from_unit, _, to_unit = input().split()
    print(translator(float(length), from_unit, to_unit))


if __name__ == '__main__':
    main()
