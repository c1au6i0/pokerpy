from pokerpy.Converters import *


class Card:
    """This class represents a single playing card

    rankOfKind: rank of the kind of the card
    rankOfSuit: rank of the suit of the card    """

    def __init__(self, conv: RankConverter, rankTuple: tuple):
        if rankTuple[0] in range(len(conv.kind)) and rankTuple[1] in range(4):
            self.rankOfKind, self.rankOfSuit = rankTuple
            self._kind = conv.kind[self.rankOfKind]
            self._suit = conv.suit[self.rankOfSuit]
            # define the name of the Card (kind and suit)
            self.name = '{} {}'.format(self._kind, self._suit)
            self.selected = False
            self.facedDown = True
            self.placeOnPlayingBoard = 0
        else:
            return False

    def __str__(self):
        return self.name
        # return self.rankTuple

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









