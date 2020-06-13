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
        self._bestCards = []
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
            self._bestCards.extend(_fours[-1])
            _name = 'Four of a kind'
        elif len(_threes) >= 1:
            if len(_threes) > 1:
                _pairFromThree = _threes[-2]
                _pairFromThree.__delitem__(0)
                _pairs.append(_pairFromThree)
                _pairs.sort()
            if len(_pairs) >= 1:
                self._bestCards.extend(_pairs[-1])
                self._bestCards.extend(_threes[-1])
                _name = 'Full house'
            else:
                self._bestCards.extend(_threes[0])
                _name = 'Three of a kind'
        elif len(_pairs) > 1:
            self._bestCards.extend(_pairs[-2])
            self._bestCards.extend(_pairs[-1])
            _name = 'Two pair'
        elif len(_pairs) == 1:
            self._bestCards.extend(_pairs[0])
            _name = 'Pair'
        else:
            _name = 'High card'
        # Extending _bestCards with sorted _kickers
        self._bestCards = self.kickers() + self._bestCards
        _numBestCards = len(self._bestCards)
        # Taking just the last 5 cards
        if _numBestCards > 5:
            self._bestCards = self._bestCards[(_numBestCards-5):_numBestCards]
        return self._conv.score.index(_name)

    def kickers(self):
        _kickers = []
        _kickers.extend(self.cards)
        # Remove _bestCards from _kickers
        for _card in self._bestCards:
            _kickers.remove(_card)
        _kickers.sort()
        return _kickers

    def straightScore(self):
        _straightCounter = 1
        _cardDifference = 0
        _name = 'High card'
        _sortedCards = []
        _sortedCards.extend(self.cards)
        _sortedCards.sort()
        _sortedCards.reverse()
        # Looping all cards, starting from the second
        for n in range(0, len(_sortedCards)-1):
            _cardDifference = _sortedCards[n].rankOfKind - _sortedCards[n+1].rankOfKind
            if _cardDifference == 0:
                pass
            elif _cardDifference == 1:
                _straightCounter += 1
                self._straightCards.append(_sortedCards[n])
            elif _cardDifference > 1:
                _straightCounter = 1
                self._straightCards.clear()
            if _straightCounter == 5:
                _name = 'Straight'
                self._straightCards.append(_sortedCards[n+1])
                self._straightCards.reverse()
                break
        return self._conv.score.index(_name)

    def Score(self):
        _suitScore = self.suitScore()
        _kindScore = self.kindScore()
        _straightScore = self.straightScore()
        if _suitScore > _kindScore:
            if _suitScore > _straightScore:
                _name = self._conv.score[_suitScore]
                self._bestCards = self._suitCards
            else:
                _name = self._conv.score[_straightScore]
                self._bestCards = self._straightCards
        else:
            if _straightScore > _kindScore:
                _name = self._conv.score[_straightScore]
                self._bestCards = self._straightCards
            else:
                _name = self._conv.score[_kindScore]

        _name = _name + ': '
        for _card in self._bestCards:
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


