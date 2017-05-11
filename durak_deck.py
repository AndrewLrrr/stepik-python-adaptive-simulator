"""
A durak deck contains 36 cards. Each card has a suit of either clubs, diamonds, hearts,
or spades (denoted C, D, H, S).
Each card also has a value of either 6 through 10, jack, queen, king, or ace
(denoted 6, 7, 8, 9, 10, J, Q, K, A).
For scoring purposes card values are ordered as above, with 6 having the lowest and ace
the highest value.

Напишите программу, которая определяет, бьёт ли одна карта другую.
Если встречаются две карты одной масти, то побеждает та, у которой выше значение;
Если карты разных мастей, то карта, имеющая козырную масть, побеждает;
Если карты разных мастей и нет козырных, то никто не побеждает.

Формат ввода:
На первой строке через пробел указываются две карты в формате <значение><масть>, а на следующей
строке указывается козырная масть.

Формат вывода:
Программа должна вывести слово
First, если первая карта бьёт вторую,
Second, если вторая карта бьёт первую,
Error, если ни одна из карт не может побить другую.
"""

import collections

Card = collections.namedtuple('Card', ['rank', 'suit', 'weight'])


class Deck:
    ranks = [str(n) for n in range(6, 11)] + list('JQKA')
    suites = 'C D H S'.split()

    def __init__(self):
        self._cards = [Card(rank, suit, idx + 1) for suit in self.suites for idx, rank in enumerate(self.ranks)]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]

    def find(self, card):
        return [item for item in self._cards if item.rank + item.suit == card][0]


def get_winner(cards, trump):
    deck = Deck()

    card_1, card_2 = [card.strip() for card in cards.split()]

    weight_1 = deck.find(card_1).weight
    weight_2 = deck.find(card_2).weight
    suit_1 = card_1[-1::]
    suit_2 = card_2[-1::]

    if suit_1 != trump and suit_2 != trump and suit_1 != suit_2:
        weight_1 = weight_2 = 0
    else:
        if suit_1 == trump:
            weight_1 *= 10
        if suit_2 == trump:
            weight_2 *= 10

    message = 'Error'

    if weight_1 > weight_2:
        message = 'First'
    elif weight_1 < weight_2:
        message = 'Second'

    return message


def main():
    print(get_winner(input(), input()))


if __name__ == '__main__':
    main()
