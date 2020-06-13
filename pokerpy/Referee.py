from pokerpy.Converters import CardRankConverter
from pokerpy.ManyCards import SetOfCards
from pokerpy.Players import Player

# TO DO: erase everything


class MatchCounter:
    def __init__(self, conv: CardRankConverter):
        self._conv = conv

    def scoreTester(self, setOfCards: SetOfCards):
        setOfCards.sortByKind()
        return self.__sameSuitList(setOfCards), self.__sameKindList(setOfCards)

    def playerScore(self, player: Player):
        player.playerCards.sortByKind()
        return self.__sameSuitList(player.playerCards), self.__sameKindList(player.playerCards)

    # next methods could be part of Class SetOfCards
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


# WIP
# move next class in SetOfCards?
class KindScoreReader:
    kindScores = {}
    kickers = []

    def read(self, setOfCards: SetOfCards):
        setOfCards.sortByKind()
        lenght = len(setOfCards.cards)
        for n in range(1, lenght):
            if setOfCards.cards[n].kind == setOfCards.cards[n-1].kind:
                # ugly code :(
                self.kindScores.append(setOfCards.cards[n])
                self.kindScores.append(setOfCards.cards[n-1])
        for _card in setOfCards:
            if not (_card in self.kindScores):
                self.kickers.append(_card)
