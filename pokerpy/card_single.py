from pokerpy.converters import *
from pokerpy.rules import *


class Card:
    """This class represents a single playing card

    rankOfKind: rank of the kind of the card
    rankOfSuit: rank of the suit of the card    """

    _conv: CardRankConverter

    # Why tuple as input and not a couple o var?
    def __init__(self, kind, suit):
        if kind in range(len(Card._conv.kind)) and suit in range(4):
            self.rankOfKind = kind
            self.rankOfSuit = suit
            self._kind = Card._conv.kind[kind]
            self._suit = Card._conv.suit[suit]
            self.selected = False
            self.facedDown = True
            self.placeOnPlayingBoard = 0
        else:
            return False

    def importConverter(conv: CardRankConverter):
        Card._conv = conv

    #  __repr__ insted of __str__
    def __repr__(self):
        return self.name

    @property
    def name(self):
        return '{} {}'.format(self._kind, self._suit)

    def __eq__(self, other):
        # Operator '=='
        # Returns true if rankOfKind and rankOfSuit are the same
        # add If applySuitRanking
        return self.rankOfKind == other.rankOfKind and self.rankOfSuit == other.rankOfSuit

    def __lt__(self, other):
        # Operator '<'
        # Returns true if the other card has higher rank
        # add If applySuitRanking
        if self == other:
            return False
        else:
            if self.rankOfKind < other.rankOfKind:
                return True
            elif self.rankOfKind > other.rankOfKind:
                return False
            else:
                if self.rankOfSuit < other.rankOfSuit:
                    return True
                elif self.rankOfSuit > other.rankOfSuit:
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









