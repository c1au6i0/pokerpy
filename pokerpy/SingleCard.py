# from pokerpy.Converter import suitSymbol
# from pokerpy.Converter import kindSymbol
from pokerpy.Converters import RankConverter


class Card:
    """This class represents a single playing card

    kindRank: rank of the kind of the card
    suitRank: rank of the suit of the card    """

    def __init__(self, conv: RankConverter, rankTuple: tuple):
        if rankTuple[0] in range(13) and rankTuple[1] in range(4):
            self.rankTuple = rankTuple
            self.kindRank = self.rankTuple[0]
            self._kind = conv.kind[self.kindRank]
            self.suitRank = rankTuple[1]
            self._suit = conv.suit[self.suitRank]
            # define the name of the Card (kind and suit)
            self.name = '{} {}'.format(self._kind, self._suit)
            # define the other variables
            # have I to define these variables with "def" ?
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
        # Returns true if kindRank and suitRank are the same
        # add If applySuitRanking
        return self.kindRank == other.kindRank and self.suitRank == other.suitRank

    def __lt__(self, other):
        # Operator '<'
        # Returns true if the other card has higher rank
        # add If applySuitRanking
        if self == other:
            return False
        else:
            if self.kindRank < other.kindRank:
                return True
            elif self.kindRank > other.kindRank:
                return False
            else:
                if self.suitRank < other.suitRank:
                    return True
                elif self.suitRank > other.suitRank:
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









