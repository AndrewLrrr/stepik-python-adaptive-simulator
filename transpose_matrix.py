"""
Напишите программу, которая принимает на вход матрицу, выполняет её транспонирование и выводит результат.

Формат ввода:
В первой строке указываются два целых числа nn и mm, количество строк и столбцов, соответственно.
Далее следуют nn строк, содержащих по mm целых чисел, разделённых пробелом.

Формат вывода:
Программа должна вывести mm строк содержимого транспонированной матрицы. Элементы матрицы стоит разделять пробелом.

Sample Input 1:
2 3
1 2 3
4 5 6
Sample Output 1:
1 4
2 5
3 6
Sample Input 2:
2 2
1 2
3 4
Sample Output 2:
1 3
2 4
"""


def transpose_matrix(matrix, n, m):
    transposed_matrix = [[0] * n for i in range(m)]
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            transposed_matrix[j][i] = val
    return transposed_matrix


def main():
    n, m = map(int, input().split())
    matrix = []
    for i in range(n):
        matrix.append(input().split())
    for row in transpose_matrix(matrix, n, m):
        print(*row)


if __name__ == '__main__':
    main()
