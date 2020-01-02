"""
A poker deck contains 52 cards. Each card has a suit of either clubs, diamonds, hearts, or spades (denoted C, D, H, S).
Each card also has a value of either 2 through 10, jack, queen, king, or ace (denoted 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q,
K, A).
For scoring purposes card values are ordered as above, with 2 having the lowest and ace the highest value.
The suit has no impact on value.

A poker hand consists of five cards. Poker hands are ranked by the following partial order from lowest to highest.

Sample Input:
10C JC QC KC AC

Sample Output:
Royal Flush
"""
import collections
import functools


POKER_HANDS = [
    'High Card',
    'Pair',
    'Two Pairs',
    'Three of a Kind',
    'Straight',
    'Flush',
    'Full House',
    'Four of a Kind',
    'Straight Flush',
    'Royal Flush',
]


def weight(w):
    def wrapper(f):
        @functools.wraps(f)
        def get_weight(*args, **kwargs):
            r = f(*args, **kwargs)
            return w if r else 0
        return get_weight
    return wrapper


class Poker:
    VALUES_MAP = {
        'J': 11,
        'Q': 12,
        'K': 13,
        'A': 14,
    }

    def __init__(self, cards):
        self._cards = cards.split()
        self._suites = [v[-1] for v in self._cards]
        self._values = []
        for card in self._cards:
            if card[0] in self.VALUES_MAP:
                self._values.append(self.VALUES_MAP[card[:-1]])
            else:
                self._values.append(int(card[:-1]))

    def get_best_poker_hand(self):
        return max(
            self.hight_card(),
            self.pair(),
            self.two_pairs(),
            self.three_of_a_kind(),
            self.straight(),
            self.flush(),
            self.full_house(),
            self.four_of_a_kind(),
            self.straight_flush(),
            self.royal_flush(),
        )

    @weight(1)
    def hight_card(self):
        """
        High Card
        Hands which do not fit any higher category are ranked by the value of their highest card.
        """
        return True

    @weight(2)
    def pair(self):
        """
        Pair
        Two of the five cards in the hand have the same value.
        """
        return len(set(self._values)) == 4

    @weight(3)
    def two_pairs(self):
        """
        Two Pairs
        The hand contains two different pairs.
        """
        r = collections.Counter(self._values)
        return len(r) == 3 and 2 in r.values()

    @weight(4)
    def three_of_a_kind(self):
        """
        Three of a Kind
        Three of the cards in the hand have the same value.
        """
        r = collections.Counter(self._values)
        return 3 in r.values()

    @weight(5)
    def straight(self):
        """
        Straight
        Hand contains five cards with consecutive values.
        """
        return max(self._values) - min(self._values) == 4

    @weight(6)
    def flush(self):
        """
        Flush
        Hand contains five cards of the same suit.
        """
        return len(set(self._suites)) == 1

    @weight(7)
    def full_house(self):
        """
        Full House
        Three cards of the same value, with the remaining two cards forming a pair.
        """
        r = collections.Counter(self._values)
        return 3 in r.values() and len(r) == 2

    @weight(8)
    def four_of_a_kind(self):
        """
        Four of a Kind
        Four cards with the same value.
        """
        r = collections.Counter(self._values)
        return 4 in r.values()

    @weight(9)
    def straight_flush(self):
        """
        Straight Flush
        Five cards of the same suit in numerical order.
        """
        return bool(self.straight()) and bool(self.flush())

    @weight(10)
    def royal_flush(self):
        """
        Royal Flush
        Consists of the ace, king, queen, jack and ten of a suit.
        """
        return bool(self.straight_flush()) and min(self._values) == 10


class TestPoker:
    def test_get_best_poker_hand(self):
        self.assert_best_poker_hand('10D 7S QH JD 9C', 'High Card')
        self.assert_best_poker_hand('10D 7S QH JD 7C', 'Pair')
        self.assert_best_poker_hand('10D 7H QH QD 7C', 'Two Pairs')
        self.assert_best_poker_hand('10D 7S 7H 7H QC', 'Three of a Kind')
        self.assert_best_poker_hand('10D 9S JH QH KC', 'Straight')
        self.assert_best_poker_hand('10D 7S 7H 7H 10C', 'Full House')
        self.assert_best_poker_hand('JC JD JH JS 10C', 'Four of a Kind')
        self.assert_best_poker_hand('7C 8C 9C JC 10C', 'Straight Flush')
        self.assert_best_poker_hand('10C JC QC KC AC', 'Royal Flush')
        print('Success!')

    @classmethod
    def assert_best_poker_hand(cls, cards, expected):
        res = POKER_HANDS[Poker(cards).get_best_poker_hand() - 1]
        if res != expected:
            raise AssertionError(res, '!=', expected)


def main():
    inp = input()
    if inp == 'test':
        TestPoker().test_get_best_poker_hand()
    else:
        print(POKER_HANDS[Poker(inp).get_best_poker_hand() - 1])


if __name__ == '__main__':
    main()
