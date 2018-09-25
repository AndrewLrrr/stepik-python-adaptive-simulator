"""
Напишите программу, вычисляющую следующее состояние поля для Game of life. 

Поле представляет собой прямоугольник, причём для крайних клеток поля соседними являются клетки с противоположного 
конца (поле представляет собой тор).

Формат ввода:
На первой строке указаны два целых числа через пробел -- высота и ширина поля. 
В следующих строках подаётся состояние поля. Точка "." обозначает мёртвую клетку, символ "X" − живую. 

Формат вывода:
Следующее состояние поля, используя те же обозначения, что использовались на вводе.

Sample Input 1:
5 5
.....
..X..
...X.
.XXX.
.....

Sample Output 1:
.....
.....
.X.X.
..XX.
..X..

Sample Input 2:
5 5
.....
.....
.XXX.
.....
.....

Sample Output 2:
.....
..X..
..X..
..X..
.....

Sample Input 3:
5 6
...XX.
.XX...
..X...
XX....
X..XX.

Sample Output 3:
.X..XX
.XX...
X.X...
XXXX.X
XXXXX.
"""


class GameOfLife:
    def __init__(self, size_n, size_m, field):
        self._size_n = size_n
        self._size_m = size_m
        if isinstance(field, str):
            self._field = []
            for line in map(lambda x: x.strip(), field.split('\n')):
                if line:
                    self._field.append(list(line))
        else:
            self._field = field
        self._memo = [[0] * size_m for _ in range(size_n)]

    def to_string(self):
        return '\n'.join([''.join(s) for s in self._field])

    def next_generation(self):
        for n in range(len(self._field)):
            for m in range(len(self._field[0])):
                counter = 0
                counter += self._look_top(n, m)
                counter += self._look_top_and_back(n, m)
                counter += self._look_top_and_forward(n, m)
                counter += self._look_bottom(n, m)
                counter += self._look_bottom_and_back(n, m)
                counter += self._look_bottom_and_forward(n, m)
                counter += self._look_back(n, m)
                counter += self._look_forward(n, m)
                self._memo[n][m] = counter

        for n in range(len(self._field)):
            for m in range(len(self._field[0])):
                cell = self._field[n][m]
                if self._memo[n][m] == 3 and cell == '.':
                    self._field[n][m] = 'X'
                elif 2 <= self._memo[n][m] <= 3 and cell == 'X':
                    continue
                else:
                    self._field[n][m] = '.'

    def _check_cell(self, n, m):
        return 1 if self._field[n][m] == 'X' else 0

    def _look_top(self, n, m):
        return self._check_cell(n - 1, m)

    def _look_top_and_back(self, n, m):
        return self._check_cell(n - 1, m - 1)

    def _look_top_and_forward(self, n, m):
        if m == self._size_m - 1:
            m = -1
        return self._check_cell(n - 1, m + 1)

    def _look_bottom(self, n, m):
        if n == self._size_n - 1:
            n = -1
        return self._check_cell(n + 1, m)

    def _look_bottom_and_back(self, n, m):
        if n == self._size_n - 1:
            n = -1
        return self._check_cell(n + 1, m - 1)

    def _look_bottom_and_forward(self, n, m):
        if n == self._size_n - 1:
            n = -1
        if m == self._size_m - 1:
            m = -1
        return self._check_cell(n + 1, m + 1)

    def _look_back(self, n, m):
        return self._check_cell(n, m - 1)

    def _look_forward(self, n, m):
        if m == self._size_m - 1:
            m = -1
        return self._check_cell(n, m + 1)


def main():
    n, m = [int(i) for i in input().split()]
    field = []
    for i in range(n):
        field.append(list(input()))

    game = GameOfLife(n, m, field)
    game.next_generation()

    print(game.to_string())


if __name__ == '__main__':
    main()
