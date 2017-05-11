"""
Поле для игры сапёр представляет собой сетку размером n×mn×m. В ячейке сетки может находиться или отсутствовать мина.

Напишите программу, которая выводит "решённое" поле, т.е. для каждой ячейки, не являющейся миной, указывается
число мин, находящихся в соседних ячейках (учитывая диагональные направления)

Формат ввода:
На первой строке указываются два натуральных числа 1≤n,m≤1001≤n,m≤100, после чего в nn строках содержится
описание поля в виде последовательности точек '.' и звёздочек '*', где точка означает пустую ячейку, а
звёздочка − ячейку с миной.

Формат вывода:
nn строк поля, в каждой ячейке которого будет либо число от 0 до 8, либо мина (обозначенная символом "*"),
при этом число означает количество мин в соседних ячейках поля.
"""


class MineField:
    def __init__(self, size_n, size_m, field):
        self.__size_n = size_n
        self.__size_m = size_m
        self.__fill_field(field)
        self.__build_field()

    def __getitem__(self, item):
        return ''.join([str(i) for i in self.__field[item]])

    def to_string(self):
        result = ''
        for row in self.__field:
            result += ''.join([str(i) for i in row]) + '\n'

        return result

    def __fill_field(self, field):
        self.__field = []
        for row in field:
            self.__field.append(['*' if i == '*' else 0 for i in row])

    def __build_field(self):
        for n, row in enumerate(self.__field):
            for m, cell in enumerate(row):
                if cell != '*':
                    self.__field[n][m] += self.__look_top(n, m)
                    self.__field[n][m] += self.__look_top_and_back(n, m)
                    self.__field[n][m] += self.__look_top_and_forward(n, m)
                    self.__field[n][m] += self.__look_bottom(n, m)
                    self.__field[n][m] += self.__look_bottom_and_back(n, m)
                    self.__field[n][m] += self.__look_bottom_and_forward(n, m)
                    self.__field[n][m] += self.__look_back(n, m)
                    self.__field[n][m] += self.__look_forward(n, m)

    def __check_cell(self, n, m):
        return 1 if self.__field[n][m] == '*' else 0

    def __look_top(self, n, m):
        if n == 0:
            return 0
        return self.__check_cell(n - 1, m)

    def __look_top_and_back(self, n, m):
        if n == 0 or m == 0:
            return 0
        return self.__check_cell(n - 1, m - 1)

    def __look_top_and_forward(self, n, m):
        if n == 0 or m == self.__size_m - 1:
            return 0
        return self.__check_cell(n - 1, m + 1)

    def __look_bottom(self, n, m):
        if n == self.__size_n - 1:
            return 0
        return self.__check_cell(n + 1, m)

    def __look_bottom_and_back(self, n, m):
        if n == self.__size_n - 1 or m == 0:
            return 0
        return self.__check_cell(n + 1, m - 1)

    def __look_bottom_and_forward(self, n, m):
        if n == self.__size_n - 1 or m == self.__size_m - 1:
            return 0
        return self.__check_cell(n + 1, m + 1)

    def __look_back(self, n, m):
        if m == 0:
            return 0
        return self.__check_cell(n, m - 1)

    def __look_forward(self, n, m):
        if m == self.__size_m - 1:
            return 0
        return self.__check_cell(n, m + 1)


def main():
    n, m = [int(i) for i in input().split()]
    field = []
    for i in range(n):
        field.append(list(input()))

    mine_field = MineField(n, m, field)

    print(mine_field.to_string())

if __name__ == '__main__':
    main()
