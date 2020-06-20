import pandas as pd
from pokerpy.card_single import Card
from random import shuffle, randint
from pokerpy.converters import *


class Cardlist(list):

    """This is a group of cards.
        PlayerCards, Deck and Flop are Cardlist"""

    conv: CardConverter
    cscore: ScoreConverter

    def __str__(self):
        if not self:
            return 'No card in this group'
        else:
            _text = ''
            for _card in self:
                _text = _text + _card.name + ' '
            return _text

    @property
    def highestCard(self):
        _sorted = self
        _sorted.sort()
        return _sorted[len(self)-1]

    def createDeck(self, lowestKind=2, decks=1):
        Cardlist.cscore = ScoreConverter(lowestKind)
        Cardlist.conv = CardConverter(lowestKind)
        Card.conv = Cardlist.conv
        for k in range(len(Cardlist.conv.kind)):
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
        # remove the first 'number' cards from this Cardlist and return these Cards objects
        # number cannot be lower than zero
        number = max(0, number)
        # number cannot be higher than cards
        number = min(number, len(self))
        for i in range(number):
            self[i].selected = True
        return self.giveSelected()

    # return selected cards list (and unselect them)
    def giveSelected(self):
        _list = []
        _listForLoop = list(self)
        for _card in _listForLoop:
            if _card.selected:
                _card.selected = False
                _list.append(_card)
                self.remove(_card)
        return _list


class PlayerCards(Cardlist):
    """The group of cards owned by the player
        plus the optional common cards
        Mainly, it's a Cardlist with score evalutator and bestaCards list"""

    def __init__(self, *args):
        super().__init__(*args)
        #self.score = self.cscore.HighCard
        self.score = 0
        self.bestFiveCards = []
        self._kindCards = []
        self.straightCards = []
        self._suitCards = []

# Kind part
    # Return a list of all the cards with the same kind
    def __kindList(self, kind: int):
        _list = []
        for _card in self:
            if _card.kind == kind:
                _list.append(_card)
        return _list

    def __kindCount(self, kind: int):
        return len(self.__kindList(kind))

    # Return a list of list of 'num' cards with same kind
    def __kindGroupOf(self, num: int):
        _list = []
        for k in range(len(Cardlist.conv.kind)):
            if self.__kindCount(k) == num:
                _list.append(self.__kindList(k))
        return _list

    # return score index (HighCard/Pair/TwoPair/ThreeKind/FullHouse/FourKind)
    def __createKindCards(self):
        _score = self.cscore.HighCard
        self._kindCards = []
        _fours = self.__kindGroupOf(4)

        if len(_fours) >= 1:
            self._kindCards.extend(_fours[-1])
            _score = PlayerCards.cscore.FourKind
        else:
            _pairs = self.__kindGroupOf(2)
            _threes = self.__kindGroupOf(3)
            # There could be more than one three, if player's got more than five cards
            if len(_threes) >= 1:
                if len(_threes) > 1:
                    _pairFromThree = _threes[-2]
                    _pairFromThree.__delitem__(0)
                    _pairs.append(_pairFromThree)
                    _pairs.sort()
                if len(_pairs) >= 1:
                    self._kindCards.extend(_pairs[-1])
                    self._kindCards.extend(_threes[-1])
                    _score = PlayerCards.cscore.FullHouse
                else:
                    self._kindCards.extend(_threes[0])
                    _score = PlayerCards.cscore.ThreeKind
            elif len(_pairs) > 1:
                self._kindCards.extend(_pairs[-2])
                self._kindCards.extend(_pairs[-1])
                _score = PlayerCards.cscore.TwoPair
            elif len(_pairs) == 1:
                self._kindCards.extend(_pairs[0])
                _score = PlayerCards.cscore.Pair
            else:
                _score = PlayerCards.cscore.HighCard
        # Extending _kindCards with sorted _kickers
        self._kindCards = self.__kickers() + self._kindCards
        _numKindCards = len(self._kindCards)
        # Taking just the last 5 cards
        if _numKindCards > 5:
            self._kindCards = self._kindCards[(_numKindCards-5):_numKindCards]
        return _score

    def __kickers(self):
        _kickers = list(self)
        # Remove bestFiveCards from _kickers
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
            if _card.suit == suit:
                _list.append(_card)
        _list.sort()
        return _list

    def __suitCount(self, suit: int):
        return len(self.__suitList(suit))

    # useless?
    def __sortBySuit(self):
        _list = []
        for s in range(4):
            _list.extend(self.__suitList(s))
        return _list

    # return index score (HighCard/Flush/RoyalFlush)
    def __createSuitCards(self, preferHighestSuit=False):
        _score = PlayerCards.cscore.HighCard
        _highestCard = Card(0, 0)
        for s in range(4):
            _count = self.__suitCount(s)
            if _count >= 5:
                _tempList = self.__suitList(s)
                # Royal flush
                if _tempList.__createStraightCards() == PlayerCards.cscore.Straight:
                    # Different rules: sometimes _highestSuit is better than _highestCard
                    if _tempList.highestCard >= _highestCard or preferHighestSuit:
                        _highestCard = _tempList.highestCard
                        self._suitCards = _tempList.straightCards
                        _score = PlayerCards.cscore.RoyalFlush
                else:
                    # Flush
                    # Different rules: sometimes _highestSuit is better than _highestCard
                    if _tempList.highestCard >= _highestCard or preferHighestSuit:
                        _highestCard = _tempList.highestCard
                        # Taking just the last 5 cards
                        self._suitCards = _tempList[(_count-5):_count]
                        _score = PlayerCards.cscore.Flush
        return _score

# TO DO
# Straight part
    def __straightList(self, lenght: int):
        _list = []
        _sorted = []
        _sorted.sort()
        for n in range(len(_sorted)):
            _cardDifference = _sorted[n].kind - _sorted[n+1].kind
            if _cardDifference == -1 or _cardDifference == Cardlist.conv.aceRank:
                _list.append(_sorted[n])
            elif _cardDifference < -1:
                _list.clear()
            # Lenght is 4 because we didn't add the last card
            if len(_list) == 4:
                break
        return _list

    def noDuplicatesList(self):
        _list = PlayerCards(self)
        _list.sort()
        _eraseList = []
        for n in range(len(_list)-1):
            if _list[n].kind == _list[n+1].kind:
                _eraseList.append(n)
        _eraseList.reverse()
        for n in _eraseList:
            _list.remove(_list[n])
        return _list

    # return index score (HighCard or Straight)
    def __createStraightCards(self):
        _score = PlayerCards.cscore.HighCard
        self.straightCards = []
        # _reversedCards is the list of the reversed Cards with no pair
        _reversedCards = self.noDuplicatesList()
        _reversedCards.reverse()
        if _reversedCards[0].kind == self.conv.aceRank:
            _reversedCards.append(_reversedCards[0])
        # Looping all cards, starting from the highest
        for n in range(len(_reversedCards)-1):
            # I could create a list of indexes, THEN O create the straightCards
            _cardDifference = _reversedCards[n].kind - _reversedCards[n+1].kind
            if _cardDifference == 1 or _cardDifference == -self.conv.aceRank:
                self.straightCards.append(_reversedCards[n])
            elif _cardDifference > 1:
                self.straightCards.clear()
            # Lenght is 4 because we still didn't add the last card
            if len(self.straightCards) == 4:
                self.straightCards.append(_reversedCards[n+1])
                self.straightCards.reverse()
                _score = PlayerCards.cscore.Straight
                break
        return _score

# ScoreFinder part
    def calculateScore(self):
        self.score = max(self.__createKindCards(), self.__createSuitCards(), self.__createStraightCards())
        if self.score == self.cscore.Straight:
            self.bestFiveCards = self.straightCards
        elif self.score == self.cscore.Flush or self.score == self.cscore.RoyalFlush:
            self.bestFiveCards = self._suitCards
        else:
            self.bestFiveCards = self._kindCards

    @property
    def scoreName(self):
        _name = self.cscore.rank[self.score]
        _name = _name + ':'
        for _card in self.bestFiveCards:
            _name = _name + ' ' + _card.name
        return _name
    # change()
