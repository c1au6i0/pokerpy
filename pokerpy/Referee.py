from pokerpy.Converter import suitSymbol
from pokerpy.Converter import numberSymbol
import array as arr


class Referee:
    def __init__(self):
        self._setOfCards = None

    def pointChecker(self, setOfCards):
        self._setOfCards = setOfCards
        self._setOfCards.sort()
        return self.__flushCards(setOfCards), self.__numberCards(setOfCards)

    # erase this
    def __flushCards_OLD(self, setOfCards):
        flushArr = arr.array('i', [0, 0, 0, 0])
        for card in setOfCards.cards:
            flushArr[card.suitRank] += 1
        flushCount = max(flushArr[0], flushArr[1], flushArr[2], flushArr[3])
        flushSuit = 0
        for i in range(4):
            if flushArr[i] == flushCount:
                flushSuit = i
        return flushCount, flushSuit

    def __flushCards(self, setOfCards):
        _flushCount = 0
        _flushSuit = 0
        for i in range(4):
            _flushForSuit = self.__flushForSuit(i, setOfCards)
            if self.__flushForSuit(i, setOfCards) >= _flushCount:
                _flushSuit = i
                _flushCount = _flushForSuit
        return '{} of {}'.format(_flushCount, suitSymbol[_flushSuit])

    def __flushForSuit(self, suitRank, setOfCards):
        _flushCount = 0
        for card in setOfCards.cards:
            if card.suitRank == suitRank:
                _flushCount += 1
        return _flushCount

    def __numberCards(self, setOfCards):
        _numberCount = 0
        _text = ''
        output = []
        for i in range(13):
            _numberCount = self.__equalForNumber(i, setOfCards)
            if _numberCount > 1:
                _text = '{} of {}'.format(_numberCount, numberSymbol[i])
                output.append(_text)
        return output

    def __equalForNumber(self, numberRank, setOfCards):
        _numberCount = 0
        for card in setOfCards.cards:
            if card.numberRank == numberRank:
                _numberCount += 1
        return _numberCount


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