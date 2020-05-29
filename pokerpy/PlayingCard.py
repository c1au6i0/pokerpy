from pokerpy.Converter import suitSymbol
from pokerpy.Converter import numberSymbol


class Card:
    """This class represents a single playing card

    numberRank: rank of the number of the card
    suitRank: rank of the suit of the card

    """

    def __init__(self, numberRank, suitRank):
        if numberRank in range(13):
            self.numberRank = numberRank
            self._numberSymbol = numberSymbol[numberRank]
        if suitRank in range(4):
            self.suitRank = suitRank
            self._suitSymbol = suitSymbol[suitRank]
        elif suitRank in suitSymbol:
            self.suitRank = suitSymbol.index(suitRank)
            self._suitSymbol = suitRank
        # define the name of the Card (number and suit)
        self.name = '{} {}'.format(self._numberSymbol, self._suitSymbol)
        # define the other variables
        self.selectedForChange = False
        self.facedDown = False
        self.placeOnPlayingBoard = 0

    def __str__(self):
        return self.name

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













