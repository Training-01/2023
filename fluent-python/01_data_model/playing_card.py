import collections
from typing import Iterable

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')  # 2~10, J, Q, K, A
    suits = 'spades diamonds clubs hearts'.split()  # spades, diamonds, clubs, hearts

    def __init__(self) -> None:
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self) -> int:
        return len(self._cards)

    def __getitem__(self, position) -> Card:
        """ The getitem method is called when the object is evaluated. """
        return self._cards[position]


if __name__ == '__main__':
    deck = FrenchDeck()
    print(len(deck))
    print(deck[0])
    print(deck[-1])

    print(deck[:3])

    print(dir(deck))

    print(isinstance(deck, Iterable))  # False  ，有__iter__方法

    for i in deck:
        print(i)

    


