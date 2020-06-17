import pandas as pd
from pokerpy.card_single import Card
from random import shuffle
from pokerpy.converters import CardRankConverter


class Cardlist(list):

    """This is a group of cards
        PlayerCards, Deck and Flop are Cardlist"""

    _conv: CardRankConverter

    def __str__(self):
        if not self:
            return 'No card in this group'
        else:
            _text = ''
            for _card in self:
                _text = _text + _card.name + ' '
            return _text

    def createDeck(self, lowestKind=2, decks=1):
        Cardlist._conv = CardRankConverter(lowestKind)
        Card.initialize(Cardlist._conv)
        for k in range(len(Cardlist._conv.kind)):
            for s in range(4):
                for d in range(decks):
                    singleCard = Card(k, s)
                    self.append(singleCard)

    def shuffle(self):
        shuffle(self)

    # useless?
    def selected(self):
        _list = Cardlist()
        for _card in self:
            if _card.selected:
                _list.append(_card)
        return _list

    def selectCard(self, index):
        self[index].selected = True

    def unselectCard(self, index: int):
        self[index].selected = False

# Take and give methods
    def giveOne(self, index=0):
        if index in range(0, len(self)):
            _card = self[index]
            self.remove(self[index])
        return _card

    def giveMany(self, number=5):
        # remove the first 'number' cards from this SetOfCards and return these Cards objects
        _list = Cardlist()
        # number cannot be lower than zero, nor higher than cards
        number = max(0, number)
        number = min(number, len(self))
        for i in range(number):
            _list.append(self.giveOne(0))
        return _list

    # useless?
    def giveSelected(self):
        _list = Cardlist()
        for _card in self:
            if _card.selected:
                _list.append(_card)
        return _list

    def takeCards(self, cardlist: list):
        self.extend(cardlist)

# Kind part
    # Return a list of all the cards with the same kind
    def kindList(self, kind: int):
        _list = Cardlist()
        for _card in self:
            if _card.rankOfKind == kind:
                _list.append(_card)
        return _list

    def kindCount(self, kind: int):
        return len(self.kindList(kind))

    # Return a list of list of 'num' cards with same kind
    def kindGroupOf(self, num: int):
        _list = Cardlist()
        for k in range(0, len(Cardlist._conv.kind)):
            if self.kindCount(k) == num:
                _list.append(self.kindList(k))
        return _list

# Suit part
    # Return a list of all the cards with the same suit
    def suitList(self, suit: int):
        _list = Cardlist()
        for _card in self:
            if _card.rankOfSuit == suit:
                _list.append(_card)
        return _list

    def suitCount(self, suit: int):
        return len(self.suitList(suit))

    # useless?
    def sortBySuit(self):
        _list = Cardlist()
        for s in range(0, 4):
            _list.extend(self.suitList(s))
        return _list

# TO DO
# Straight part
    def straightList(self, minLenght: int):
        _list = Cardlist()
        for _card in self:
            if _card.rankOfKind == minLenght:
                _list.append(_card)
        return _list


class PlayerCards(Cardlist):
    """The group of cards owned by the player
        plus the optional common cards
        Mainly, it's a Cardlist with score evalutator and bestaCards list"""

    def __init__(self, *args):
        super().__init__(*args)
        self.score = 0
        self.bestCards = []
        self._kindCards = []
        self._straightCards = []
        self._suitCards = []

# KindFinder part
    def __kindScore(self):
        self._kindCards = []
        _name = ''
        _pairs = self.kindGroupOf(2)
        _threes = self.kindGroupOf(3)
        _fours = self.kindGroupOf(4)

        if len(_fours) >= 1:
            self._kindCards.extend(_fours[-1])
            _name = 'Four of a kind'
        # There could be more than one three, if player's got more than five cards
        elif len(_threes) >= 1:
            if len(_threes) > 1:
                _pairFromThree = _threes[-2]
                _pairFromThree.__delitem__(0)
                _pairs.append(_pairFromThree)
                _pairs.sort()
            if len(_pairs) >= 1:
                self._kindCards.extend(_pairs[-1])
                self._kindCards.extend(_threes[-1])
                _name = 'Full house'
            else:
                self._kindCards.extend(_threes[0])
                _name = 'Three of a kind'
        elif len(_pairs) > 1:
            self._kindCards.extend(_pairs[-2])
            self._kindCards.extend(_pairs[-1])
            _name = 'Two pair'
        elif len(_pairs) == 1:
            self._kindCards.extend(_pairs[0])
            _name = 'Pair'
        else:
            _name = 'High card'
        # Cleaning
        del _pairs, _threes, _fours
        # Extending _kindCards with sorted _kickers
        self._kindCards = self.__kickers() + self._kindCards
        _numKindCards = len(self._kindCards)
        # Taking just the last 5 cards
        if _numKindCards > 5:
            self._kindCards = self._kindCards[(_numKindCards-5):_numKindCards]
        return self._conv.score.index(_name)

    def __kickers(self):
        _kickers = []
        _kickers.extend(self)
        # Remove bestCards from _kickers
        for _card in self._kindCards:
            if _card in _kickers:
                _kickers.remove(_card)
            else:
                print(_card, ' is not in list')
        _kickers.sort()
        return _kickers

# SuitFinder part

# TO DO, IT'S AT DICK
    def __suitScore(self):
        _suitCards = Cardlist()
        _name = 'High card'
        for s in range(0, 4):
            _count = self.suitCount(s)
            if _count >= 5:
                # Taking just the last 5 cards
                _suitCards = self.suitList(s)
                _suitCards = _suitCards[(_count-5):_count]
                _name = 'Flush'
        return Cardlist._conv.score.index(_name)

# StraightFinder part
    def __straightScore(self):
        self._straightCards = []
        # _reversedCards is the list of the reversed Cars with no pair
        _reversedCards = []
        _reversedCards.extend(self)
        _reversedCards.sort()
        _eraseList = []
        for n in range(0, len(_reversedCards)-1):
            if _reversedCards[n].rankOfKind == _reversedCards[n+1].rankOfKind:
                _eraseList.append(n)
        _eraseList.reverse()
        for n in _eraseList:
            _reversedCards.remove(_reversedCards[n])
        del _eraseList
        _reversedCards.reverse()
        if _reversedCards[0].rankOfKind == self._conv.aceRank:
            _reversedCards.append(_reversedCards[0])

        # Looping all cards, starting from the highest
        _name = 'High card'
        for n in range(0, len(_reversedCards)-1):
            # I could create a list of indexes, THEN O create the _straightCards
            _cardDifference = _reversedCards[n].rankOfKind - _reversedCards[n+1].rankOfKind
            if _cardDifference == 1 or _cardDifference == -self._conv.aceRank:
                self._straightCards.append(_reversedCards[n])
            elif _cardDifference > 1:
                self._straightCards.clear()
            # Lenght is 4 because we didn't add the last card
            if len(self._straightCards) == 4:
                _name = 'Straight'
                self._straightCards.append(_reversedCards[n+1])
                self._straightCards.reverse()
                break
        del _reversedCards
        return self._conv.score.index(_name)

# ScoreFinder part
    def calculateScore(self):
        self.score = max(self.__suitScore(), self.__kindScore(), self.__straightScore())
        if self.score == self._conv.score.index('Straight'):
            self.bestCards = self._straightCards
        elif self.score == self._conv.score.index('Flush'):
            self.bestCards = self._suitCards
        else:
            self.bestCards = self._kindCards
        del self._straightCards
        del self._suitCards
        del self._kindCards

    @property
    def scoreName(self):
        _name = self._conv.score[self.score]
        _name = _name + ': '
        for _card in self.bestCards:
            _name = _name + ' ' + _card.name
        return _name
    # change()
