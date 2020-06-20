import pandas as pd
from pokerpy.card_single import Card
from random import shuffle, randint
from pokerpy.converters import *


class Cardlist(list):

    """This is a group of cards.
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
        Card.importConverter(Cardlist._conv)
        for k in range(len(Cardlist._conv.kind)):
            for s in range(4):
                for d in range(decks):
                    _singleCard = Card(k, s)
                    self.append(_singleCard)

    def shuffle(self):
        shuffle(self)

    def cut(self):
        _numCards = randint(2, (len(self)-1))
        _cuttedCards = self[0:_numCards]
        for _card in _cuttedCards:
            self.remove(_card)
        self.extend(_cuttedCards)

# Give and Select methods
    # useless?
    def selectCard(self, index):
        self[index].selected = True

    # useless?
    def unselectCard(self, index: int):
        self[index].selected = False

    def give(self, number=5):
        # remove the first 'number' cards from this SetOfCards and return these Cards objects
        # number cannot be lower than zero
        number = max(0, number)
        # number cannot be higher than cards
        number = min(number, len(self))
        for i in range(0, number):
            self[i].selected = True
        return self.giveSelected()

    # useless?
    def giveSelected(self):
        _list = Cardlist()
        _listForLoop = []
        _listForLoop.extend(self)
        for _card in _listForLoop:
            if _card.selected:
                _card.selected = False
                _list.append(_card)
                self.remove(_card)
        del _listForLoop
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
        self.straightCards = []
        self._suitCards = []

# Kind part
    # Return a list of all the cards with the same kind
    def __kindList(self, kind: int):
        _list = PlayerCards()
        for _card in self:
            if _card.rankOfKind == kind:
                _list.append(_card)
        return _list

    def __kindCount(self, kind: int):
        return len(self.__kindList(kind))

    # Return a list of list of 'num' cards with same kind
    def __kindGroupOf(self, num: int):
        _list = PlayerCards()
        for k in range(0, len(Cardlist._conv.kind)):
            if self.__kindCount(k) == num:
                _list.append(self.__kindList(k))
        return _list

    def __kindScore(self):
        self._kindCards = PlayerCards()
        _name = ''
        _pairs = self.__kindGroupOf(2)
        _threes = self.__kindGroupOf(3)
        _fours = self.__kindGroupOf(4)

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

# Suit part
    # Return a list of all the cards with the same suit
    def __suitList(self, suit: int):
        _list = PlayerCards()
        for _card in self:
            if _card.rankOfSuit == suit:
                _list.append(_card)
        _list.sort()
        return _list

    def __suitCount(self, suit: int):
        return len(self.__suitList(suit))

    # useless?
    def __sortBySuit(self):
        _list = PlayerCards()
        for s in range(0, 4):
            _list.extend(self.__suitList(s))
        return _list

    def __suitScore(self):
        _name = 'High card'
        for s in range(0, 4):
            _count = self.__suitCount(s)
            if _count >= 5:
                self._suitCards = self.__suitList(s)
                _straightScore = self._suitCards.__straightScore()
                if _straightScore == self._conv.score.index('Straight'):
                    self._suitCards = self._suitCards.straightCards
                    _name = 'Royal flush'
                else:
                    # Taking just the last 5 cards
                    self._suitCards = self._suitCards[(_count-5):_count]
                    _name = 'Flush'
        return Cardlist._conv.score.index(_name)

# TO DO
# Straight part
    def __straightList(self, lenght: int):
        _list = PlayerCards()
        _sorted = PlayerCards()
        _sorted.sort()
        for n in range(0, len(_sorted)):
            _cardDifference = _sorted[n].rankOfKind - _sorted[n+1].rankOfKind
            if _cardDifference == -1 or _cardDifference == Cardlist._conv.aceRank:
                _list.append(_sorted[n])
            elif _cardDifference < -1:
                _list.clear()
            # Lenght is 4 because we didn't add the last card
            if len(_list) == 4:
                _name = 'Straight'
                break
        del _sorted
        return _list

    def __straightScore(self):
        self.straightCards = PlayerCards()
        # _reversedCards is the list of the reversed Cars with no pair
        _reversedCards = PlayerCards()
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
            # I could create a list of indexes, THEN O create the straightCards
            _cardDifference = _reversedCards[n].rankOfKind - _reversedCards[n+1].rankOfKind
            if _cardDifference == 1 or _cardDifference == -self._conv.aceRank:
                self.straightCards.append(_reversedCards[n])
            elif _cardDifference > 1:
                self.straightCards.clear()
            # Lenght is 4 because we didn't add the last card
            if len(self.straightCards) == 4:
                _name = 'Straight'
                self.straightCards.append(_reversedCards[n+1])
                self.straightCards.reverse()
                break
        del _reversedCards
        return self._conv.score.index(_name)

# ScoreFinder part
    def calculateScore(self):
        self.score = max(self.__kindScore(), self.__suitScore(), self.__straightScore())
        if self.score == self._conv.score.index('Straight'):
            self.bestCards = self.straightCards
        elif self.score == self._conv.score.index('Flush') or self.score == self._conv.score.index('Royal flush'):
            self.bestCards = self._suitCards
        else:
            self.bestCards = self._kindCards

        # del self.straightCards
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
