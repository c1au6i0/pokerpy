from pokerpy.Converters import CardRankConverter
from pokerpy.ManyCards import SetOfCards

#
class MatchCounter:
    def __init__(self, conv: CardRankConverter):
        self._conv = conv

    def pointChecker(self, setOfCards: SetOfCards):
        setOfCards.sort()
        return self.__sameSuitList(setOfCards), self.__sameKindList(setOfCards)

    def __sameSuitList(self, setOfCards: SetOfCards):
        _suitCounter = Counter()
        for i in range(4):
            _suitCounter.add(self._conv.suit[i], self.__sameSuit(i, setOfCards))
        return _suitCounter.output(3)

    def __sameSuit(self, rankOfSuit, setOfCards: SetOfCards):
        _count = 0
        for _card in setOfCards.cards:
            if _card.rankOfSuit == rankOfSuit:
                _count += 1
        return _count

    def __sameKindList(self, setOfCards: SetOfCards):
        _kindCounter = Counter()
        for i in range(len(self._conv.kind)):
            _kindCounter.add(self._conv.kind[i], self.__sameKind(i, setOfCards))
        return _kindCounter.output()

    def __sameKind(self, rankOfKind: int, setOfCards: SetOfCards):
        _count = 0
        for _card in setOfCards.cards:
            if _card.rankOfKind == rankOfKind:
                _count += 1
        return _count


# just a try
class Subgroup:
    def __init__(self, rank: int, count: int):
        self.rank = rank
        self.count = count


class Counter:
    def __init__(self):
        self.subgroupList = []

    def add(self, rank: int, count: int):
        # if count >= minCount:
        self.subgroupList.append((rank, count))

    def higherSubgroup(self):
        _higherCount = 0
        for rank, count in self.subgroupList:
            # at least a couple of matches to print it
            if count >= _higherCount:
                _higherCount = count
        return _higherCount

    def output(self, minCount=2):
        _totText = ''
        for rank, count in self.subgroupList:
            # at least a couple of matches to print it
            if count >= minCount:
                _text = '{} of {}'.format(count, rank)
                if _totText == '':
                    _totText = _text
                else:
                    _totText = _totText + ' and ' + _text
        return _totText


class Point:
    point1 = None
    point2 = None
    kicker1 = None
    kicker2 = None
    kicker3 = None


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