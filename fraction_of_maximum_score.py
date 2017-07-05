"""
Напишите программу, которая вычисляет долю студентов, получивших оценку A.

Используется пятибальная система оценивания с оценками A, B, C, D, F.

Формат ввода:
Строка, в которой через пробел записаны оценки студентов. Оценок всегда не меньше одной.

Формат вывода:
Дробное число с ровно двумя знаками после запятой.

Sample Input 1:
F B A A B C A D
Sample Output 1:
0.38
Sample Input 2:
B C B
Sample Output 2:
0.00
Sample Input 3:
A D
Sample Output 3:
0.50
"""

from collections import Counter


def fraction_of_maximum_score(scores):
    cnt = Counter()
    for score in scores:
        cnt[score] += 1
    return cnt['A'] / len(scores) if scores else 0


def main():
    scores = input().split()
    print('{0:.2f}'.format(fraction_of_maximum_score(scores)))


if __name__ == '__main__':
    main()
