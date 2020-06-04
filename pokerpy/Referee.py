from pokerpy.Converters import RankConverter
from pokerpy.ManyCards import SetOfCards


class MatchCounter:
    def __init__(self, conv: RankConverter):
        self._conv = conv

    def pointChecker(self, setOfCards: SetOfCards):
        setOfCards.sort()
        return self.__sameSuitList(setOfCards), self.__sameKindList(setOfCards)

    def __sameSuitList(self, setOfCards: SetOfCards):
        _suitCount = 0
        _text = ''
        output = []
        for i in range(4):
            _suitCount = self.__sameSuit(i, setOfCards)
            if _suitCount > 1:
                _text = '{} {}'.format(_suitCount, self._conv.suit[i])
                output.append(_text)
        return output

    def __sameSuit(self, rankOfSuit, setOfCards: SetOfCards):
        _count = 0
        for _card in setOfCards.cards:
            if _card.rankOfSuit == rankOfSuit:
                _count += 1
        return _count

    def __sameKindList(self, setOfCards: SetOfCards):
        _kindCount = 0
        _text = ''
        output = []
        for i in range(13):
            _kindCount = self.__sameKind(i, setOfCards)
            if _kindCount > 1:
                _text = '{} {}'.format(_kindCount, self._conv.kind[i])
                output.append(_text)
        return output

    def __sameKind(self, rankOfKind: int, setOfCards: SetOfCards):
        _count = 0
        for _card in setOfCards.cards:
            if _card.rankOfKind == rankOfKind:
                _count += 1
        return _count

# add "kickers"


class Counter:
    def __init__(self, kindOrSuit, rank: int, count: int):
        # kindOrSuit == 0 => kind, kindOrSuit == 1 => suit
        if kindOrSuit == 0:
            self.symbol = self._conv.kind[rank]
        else:
            self.symbol = self._conv.suit[rank]
        self.text = '{} {}'.format(count, self._conv.of, self.symbol)

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
# validOpening() : bool
# Winner()
# validFacedUpCards(): bool