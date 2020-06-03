from pokerpy.Converter import suitSymbol
from pokerpy.Converter import kindSymbol


class MatchCounter:
    def __init__(self):
        self._setOfCards = None

    def pointChecker(self, setOfCards):
        self._setOfCards = setOfCards
        self._setOfCards.sort()
        return self.__sameSuitList(setOfCards), self.__sameKindList(setOfCards)

    def __sameSuitList(self, setOfCards):
        _suitCount = 0
        _text = ''
        output = []
        for i in range(4):
            _suitCount = self.__sameSuit(i, setOfCards)
            if _suitCount > 1:
                _text = '{} of {}'.format(_suitCount, suitSymbol[i])
                output.append(_text)
        return output

    def __sameSuit(self, suitRank, setOfCards):
        _count = 0
        for _card in setOfCards.cards:
            if _card.suitRank == suitRank:
                _count += 1
        return _count

    def __sameKindList(self, setOfCards):
        _kindCount = 0
        _text = ''
        output = []
        for i in range(13):
            _kindCount = self.__sameKind(i, setOfCards)
            if _kindCount > 1:
                _text = '{} of {}'.format(_kindCount, kindSymbol[i])
                output.append(_text)
        return output

    def __sameKind(self, kindRank, setOfCards):
        _count = 0
        for _card in setOfCards.cards:
            if _card.kindRank == kindRank:
                _count += 1
        return _count


class Counter:
    def __init__(self, kindOrSuit, rank, count):
        # kindOrSuit == 0 => kind, kindOrSuit == 1 => suit
        if kindOrSuit == 0:
            self.symbol = kindSymbol(rank)
        else:
            self.symbol = suitSymbol(rank)
        self.text = '{} of {}'.format(count, self.symbol)

# italianPointRank = ('High card', 'Pair', 'Two pair', 'Three of a kind', 'Straight', 'Full house',                    'Flush', 'Four of a kind', 'Straight flush', 'Royal flush')
# americanPointRank = ('High card', 'Pair', 'Two pair', 'Three of a kind', 'Straight', 'Flush',                     'Full house', 'Four of a kind', 'Straight flush', 'Royal flush')
# almostPoint=(puntoIntermedio,scalaAdIncastro,scalaBilaterale,4/5 colore,4/5 ScalaReale,4/5 ScalaReale bilaterale)

# fullVsFlush: bool
# straightFlushVsStraightFlush:  
# minOpen: (JJ, QQ, KK)
# opening: type
# minCardDeck
# specialCards
# ruleNextCard
# ruleSuit
# fullVsSelf
# percentageOfPoker
# percentageOfColour
# percentageOfScala
# validOpening() : bool
# Winner()
# validFacedUpCards(): bool
# readDeck(deck)