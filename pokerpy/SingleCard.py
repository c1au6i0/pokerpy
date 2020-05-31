from pokerpy.Converter import suitSymbol
from pokerpy.Converter import numberSymbol


class Card:
    """This class represents a single playing card

    numberRank: rank of the number of the card
    suitRank: rank of the suit of the card    """

    def __init__(self, rankTuple):
        if rankTuple[0] in range(13) and rankTuple[1] in range(4):
            self.rankTuple = rankTuple
            self.numberRank = self.rankTuple[0]
            self._numberSymbol = numberSymbol[self.numberRank]
            self.suitRank = rankTuple[1]
            self._suitSymbol = suitSymbol[self.suitRank]
            # define the name of the Card (number and suit)
            self.name = '{} {}'.format(self._numberSymbol, self._suitSymbol)
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
        # Returns true if numberRank and suitRank are the same
        # add If applySuitRanking
        return self.numberRank == other.numberRank and self.suitRank == other.suitRank

    def __lt__(self, other):
        # Operator '<'
        # Returns true if the other card has higher rank
        # add If applySuitRanking
        if self == other:
            return False
        else:
            if self.numberRank < other.numberRank:
                return True
            elif self.numberRank > other.numberRank:
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









