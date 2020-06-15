import pandas as pd
from pokerpy.card_single import Card
from random import shuffle
from pokerpy.converters import CardRankConverter


class Cardlist(list):
    # def give
    _conv: CardRankConverter

#    def __new__(cls, *args):
#        super().__new__(cls, *args)
#        cls.conv: CardRankConverter

    def importConverter(conv: CardRankConverter):
        Cardlist._conv = conv

    def __str__(self):
        if not self:
            return 'No card in this group'
        else:
            _text = ''
            for _card in self:
                _text = _text + _card.name + ' '
            return _text

    # useless?
    def selected(self):
        _list = Cardlist()
        for _card in self:
            if _card.selected:
                _list.append(_card)
        return _list

# Kind part
    # Return a list of all the cards with the same kind
    def kindList(self, kind: int):
        _list = Cardlist()
        _list.sort()
        for _card in self:
            if _card.rankOfKind == kind:
                _list.append(_card)
        return _list

    def kindCount(self, kind: int):
        return len(self.kindList(kind))

    # Return a list of list of 'num' cards with same kind
    def groupOf(self, num: int):
        _list = []
        _list.sort()
        for k in range(0, len(Cardlist._conv.kind)):
            if self.kindCount(k) == num:
                _list.append(self.kindList(k))
        return _list

# Suit part
    # Return a list of all the cards with the same suit
    def suitList(self, suit: int):
        _list = Cardlist()
        _list.sort()
        for _card in self:
            if _card.rankOfSuit == suit:
                _list.append(_card)
        return _list

    def suitCount(self, suit: int):
        return len(self.suitList(suit))

# TO DO, IT'S AT DICK
    def suitScore(self):
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

    # faceDownCards: int(?)
    # faceUpCards: int(?)
    # selectedCards
    # show()


class CommonCards(SetOfCards):
    """This is the group of card that could be used by every active players
    This class is used just in Texas hold 'em and Telesina
    """
    def __init__(self, conv: CardRankConverter):
        super().__init__(conv)


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


class PlayerCards(SetOfCards):
    """The group of cards owned by the player
        plus the optional common cards"""

    def __init__(self, conv: CardRankConverter):
        super().__init__(conv)
        self.score = 0
        self.bestCards = []
        self._kindCards = []
        self._straightCards = []
        self._suitCards = []

    def selectCard(self, index):
        self.cards[index].selected = True

    def unselectCard(self, index: int):
        self.cards[index].selected = False

# KindFinder part
    def __sameKindList(self, cards: list, rankOfKind: int):
        _list = []
        for _card in cards:
            if _card.rankOfKind == rankOfKind:
                _list.append(_card)
        return _list

    def __kindScore(self):
        self._kindCards = []
        _name = ''
        _pairs = []
        _threes = []
        _fours = []

        for k in range(0, len(self._conv.kind)):
            _cardList = self.__sameKindList(self.cards, k)
            _numCardsInList = len(_cardList)
            if _numCardsInList == 2:
                _pairs.append(_cardList)
            elif _numCardsInList == 3:
                _threes.append(_cardList)
            elif _numCardsInList == 4:
                _fours.append(_cardList)

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
        _kickers.extend(self.cards)
        # Remove bestCards from _kickers
        for _card in self._kindCards:
            if _card in _kickers:
                _kickers.remove(_card)
            else:
                print(_card, ' is not in list')
        _kickers.sort()
        return _kickers

# SuitFinder part
    def __sameSuitList(self, cards: list, rankOfKind: int):
        _list = []
        for _card in cards:
            if _card.rankOfSuit == rankOfKind:
                _list.append(_card)
        return _list

    def __suitScore(self):
        self._suitCards = []
        _name = 'High card'

        for s in range(0, 4):
            _cardList = self.__sameSuitList(self.cards, s)
            _lenList = len(_cardList)
            if _lenList >= 5:
                # Taking just the last 5 cards
                self._suitCards = _cardList[(_lenList-5):_lenList]
                _name = 'Flush'
        return self._conv.score.index(_name)

# StraightFinder part

    def __straightScore(self):
        self._straightCards = []
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
