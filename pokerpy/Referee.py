from pokerpy.Converters import CardRankConverter
from pokerpy.ManyCards import SetOfCards
from pokerpy.Players import Player


class MatchCounter:
    def __init__(self, conv: CardRankConverter):
        self._conv = conv

    def scoreTester(self, setOfCards: SetOfCards):
        setOfCards.sort()
        return self.__sameSuitList(setOfCards), self.__sameKindList(setOfCards)

    def playerScore(self, player: Player):
        player.playerCards.sort()
        return self.__sameSuitList(player.playerCards), self.__sameKindList(player.playerCards)

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


# add rank in operators?
class Subgroup:
    def __init__(self, rank: int, count: int):
        self.rank = rank
        self.count = count
        self.text = '{} of {}'.format(self.count, self.rank)

    def __eq__(self, other):
        # Operator '=='
        return self.count == other.count

    def __lt__(self, other):
        # Operator '<'
        return self.count < other.count

    def __gt__(self, other):
        # Operator '>'
        return self.count > other.count

    def __le__(self, other):
        # Operator '<='
        return self < other or self == other

    def __ge__(self, other):
        # Operator '>='
        return self > other or self == other


class Counter:
    def __init__(self):
        self._subgroupList = []

    def add(self, rank: int, count: int):
        self._subgroupList.append(Subgroup(rank, count))

    def higherSubgroup(self):
        _higherSubgroup = Subgroup(0, 0)
        for _subgroup in self._subgroupList:
            # at least a couple of matches to print it
            if _subgroup >= _higherSubgroup:
                _higherSubgroup = _subgroup
        return _higherSubgroup
        # ...or: return _higherSubgroup.text

    def output(self, minCount=2):
        _totText = ''
        for _subgroup in self._subgroupList:
            # at least a couple of matches to print it
            if _subgroup.count >= minCount:
                if _totText == '':
                    _totText = _subgroup.text
                else:
                    _totText = '{} and {}'.format(_totText, _subgroup.text)
        return _totText


class Score:
    point1 = None
    point2 = None
    kicker1 = None
    kicker2 = None
    kicker3 = None

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