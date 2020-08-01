import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n)for n in range(2,11)] + list('JQKA')
    suits = 'spades diamon clubs hearts'.split()

    def __init__(self):
        self.cards = [Card(rank, suit)for suit in self.suits
                      for rank in self.ranks]

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, position):
        return self.cards[position]


x = FrenchDeck()
print(len(x))