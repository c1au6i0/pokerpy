import pandas as pd
from pokerpy.SingleCard import Card
from random import shuffle
from pokerpy.Converters import CardRankConverter

__all__ = ['SetOfCards', 'Deck', 'PlayerCards']


class SetOfCards:
    """This is a group of cards
        PlayerCards, Deck and Flop are SetOfCards"""
    
    def __init__(self, conv: CardRankConverter):
        # create the empty list of cards
        self.cards = []
        self.score = 0
        self._conv = conv

    def __len__(self):
        return len(self.cards)

    def giveSingleCard(self, index=0):
        if index in range(0, len(self.cards)):
            singleCard = self.cards[index]
            self.cards.remove(self.cards[index])
        return singleCard

    def giveCards(self, number=5):
        # remove the first 'number' cards from this SetOfCards and return these Cards objects
        givenCards = []
        # number cannot be lower than zero, nor higher than cards
        number = max(0, number)
        number = min(number, len(self.cards))
        for i in range(number):
            givenCards.append(self.giveSingleCard(0))
        return givenCards

    def giveSelectedCards(self):
        givenCards = []
        for card in self.cards:
            if card.selected:
                givenCards.append(card)
        return givenCards

    def takeCards(self, cardsList: list):
        self.cards.extend(cardsList)

    def showOnConsole(self, justSelectedCards=False):
        _text = ' | '
        if not self.cards:
            print('No card in this group')
        else:
            for card in self.cards:
                if not justSelectedCards or card.selected:
                    _text = _text + card.name + ' | '
        print(_text)

    def sortByKind(self):
        self.cards.sort()

    def sortBySuit(self):
        pass
    # faceDownCards: int(?)
    # faceUpCards: int(?)
    # selectedCards
    # show()


class PlayerCards(SetOfCards):
    """look at the class name, it's not so hard"""

    def __init__(self, conv: CardRankConverter):
        super().__init__(conv)
        self._straightCards = []
        self.bestCards = []
        self._suitCards = []

    def selectCard(self, index):
        self.cards[index].selected = True

    def unselectCard(self, index: int):
        self.cards[index].selected = False

    def __sameKindList(self, rank: int):
        _list = []
        # can you use a Comprehension?
        for _card in self.cards:
            if _card.rankOfKind == rank:
                _list.append(_card)
        return _list

    def __sameSuitList(self, rank: int):
        _list = []
        # can you use a Comprehension?
        for _card in self.cards:
            if _card.rankOfSuit == rank:
                _list.append(_card)
        return _list

    def suitScore(self):
        _name = 'High card'

        for s in range(0, 4):
            _cardList = self.__sameSuitList(s)
            if len(_cardList) >= 5:
                # Taking just the last 5 cards
                self._suitCards = _cardList[(len(_cardList)-5):len(_cardList)]
                _name = 'Flush'
        return self._conv.score.index(_name)

    def kindScore(self):
        _pairs = []
        _threes = []
        _fours = []
        _name = ''

        for k in range(0, len(self._conv.kind)):
            _cardList = self.__sameKindList(k)
            _numCardsInList = len(_cardList)
            if _numCardsInList == 2:
                _pairs.append(_cardList)
            elif _numCardsInList == 3:
                _threes.append(_cardList)
            elif _numCardsInList == 4:
                _fours.append(_cardList)

        if len(_fours) >= 1:
            self.bestCards.extend(_fours[-1])
            _name = 'Four of a kind'
        elif len(_threes) >= 1:
            if len(_threes) > 1:
                _pairFromThree = _threes[-2]
                _pairFromThree.__delitem__(0)
                _pairs.append(_pairFromThree)
                _pairs.sort()
            if len(_pairs) >= 1:
                self.bestCards.extend(_pairs[-1])
                self.bestCards.extend(_threes[-1])
                _name = 'Full house'
            else:
                self.bestCards.extend(_threes[0])
                _name = 'Three of a kind'
        elif len(_pairs) > 1:
            self.bestCards.extend(_pairs[-2])
            self.bestCards.extend(_pairs[-1])
            _name = 'Two pair'
        elif len(_pairs) == 1:
            self.bestCards.extend(_pairs[0])
            _name = 'Pair'
        else:
            _name = 'High card'
        # Extending bestCards with sorted _kickers
        self.bestCards = self.kickers() + self.bestCards
        _numBestCards = len(self.bestCards)
        # Taking just the last 5 cards
        if _numBestCards > 5:
            self.bestCards = self.bestCards[(_numBestCards-5):_numBestCards]
        return self._conv.score.index(_name)

    def kickers(self):
        _kickers = []
        _kickers.extend(self.cards)
        # Remove bestCards from _kickers
        for _card in self.bestCards:
            if _card in _kickers:
                _kickers.remove(_card)
            else:
                print(_card, ' is not in list')
        _kickers.sort()
        return _kickers

    def straightScore(self):
        # _reversedCards is the list of the reversed Cars with no pair
        _reversedCards = []
        _reversedCards.extend(self.cards)
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
            if len(self._straightCards) == 4:
                _name = 'Straight'
                self._straightCards.append(_reversedCards[n+1])
                self._straightCards.reverse()
                break
        del _reversedCards
        return self._conv.score.index(_name)

    def calculateScore(self):
        self.score = max(self.suitScore(), self.kindScore(), self.straightScore())
        if self.score == self._conv.score.index('Straight'):
            self.bestCards = self._straightCards
        elif self.score == self._conv.score.index('Flush'):
            self.bestCards = self._suitCards

    @property
    def scoreName(self):
        _name = self._conv.score[self.score]
        _name = _name + ': '
        for _card in self.bestCards:
            _name = _name + ' ' + _card.name
        return _name
    # typePoint()
    # change()
    # show()


# class Deck(SetOfCards, pd.DataFrame):
# I remove DataFrame due to problems with import abc
class Deck(SetOfCards):
    """Deck is Deck"""
    # This is the constructor
    def __init__(self, conv: CardRankConverter, decks=1):
        # decks=0 => empty deck
        # decks=2 => classic Scala40 deck
        super().__init__(conv)
        # fulfill the cards list
        for k in range(len(self._conv.kind)):
            for s in range(4):
                for d in range(decks):
                    singleCard = Card(self._conv, (k, s))
                    self.cards.append(singleCard)
        # create the rejects list (empty at start)
        self.rejects = []

    def shuffle(self):
        shuffle(self.cards)

    def remainingSuit(self, rankOfSuit: int):
        _count = 0
        for _card in self.cards:
            if _card.rankOfSuit == rankOfSuit:
                _count += 1
        return _count

    def remainingKind(self, rankOfKind: int):
        _count = 0
        for _card in self.cards:
            if _card.rankOfKind == rankOfKind:
                _count += 1
        return _count

    def takeRejects(self, cardsList: list):
        self.rejects.extend(cardsList)


class OrderRules:
    # random
    # insert
    # primaGliScarti
    # Sort()
    pass


