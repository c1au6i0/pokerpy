from pokerpy.converters import *
from pokerpy.rules import *


class Card:
    """This class represents a single playing card

    kind: rank of the kind of the card
    suit: rank of the suit of the card    """

    conv: CardConverter

    # Why tuple as input and not a couple o var?
    def __init__(self, kind, suit):
        if kind in range(len(Card.conv.kind)) and suit in range(4):
            self.kind = kind
            self.suit = suit
            self.name = '{} {}'.format(Card.conv.kind[kind], Card.conv.suit[suit])
            self.selected = False
            self.facedDown = True
            self.placeOnPlayingBoard = 0
        else:
            return False

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









