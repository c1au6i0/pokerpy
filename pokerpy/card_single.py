class Card:
    """This class represents a single playing card

    kind: rank of the kind of the card (from 2, 7, 8, 9 or 10 to 14 = Ace)
    suit: rank of the suit of the card (from 0 = ♠ to 3 = ♡)
    name: card name in symbolic format
    """

    #_symbol_of_suit = (chr(9824), chr(9827), chr(9830), chr(9829))
    #_symbol_of_suit = ("♠", "♣", "♢", "♡")
    _symbol_of_suit = ('♤', '♧', '♦', '♥')
    #_symbol_of_suit = (chr(9824), chr(9827), chr(9830), chr(9829))
    # "0" and "1" are useless, but usefull to recognize fast the correct symbol
    _symbol_of_kind = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")

    def __init__(self, kind, suit):
        self.kind = kind
        self.suit = suit
        self.name = '{} {}'.format(self._symbol_of_kind[kind], self._symbol_of_suit[suit])
        self.selected = False
        self.faced_down = True

    #  __repr__ insted of __str__
    def __repr__(self):
        return self.name

    def __eq__(self, other):
        # Operator '=='
        # Returns true if kind and suit are the same
        # add If applySuitRanking
        return self.kind == other.kind and self.suit == other.suit

    def __lt__(self, other):
        # Operator '<'
        # Returns true if the other card has higher rank
        # add If applySuitRanking
        if self == other:
            return False
        else:
            if self.kind < other.kind:
                return True
            elif self.kind > other.kind:
                return False
            else:
                if self.suit < other.suit:
                    return True
                elif self.suit > other.suit:
                    return False

    def __gt__(self, other):
        # Operator '>'
        # Returns true if the other card has higher rank
        # add If applySuitRanking
        if self == other:
            return False
        else:
            return not (self < other)

    def __le__(self, other):
        # Operator '<='
        # Returns true if the other card has higher or equal rank
        return (self < other) or (self == other)

    def __ge__(self, other):
        # Operator '>='
        # Returns true if the other card has lower or equal rank
        return (self > other) or (self == other)

    def image(self):
        # here is the .jpg or .ico or .png file
        pass









