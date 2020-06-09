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

    def sort(self):
        self.cards.sort()
    # faceDownCards: int(?)
    # faceUpCards: int(?)
    # selectedCards
    # show()


class PlayerCards(SetOfCards):
    """look at the class name, it's not so hard"""
    def selectCard(self, index):
        self.cards[index].selected = True

    def unselectCard(self, index: int):
        self.cards[index].selected = False

    # typePoint()
    # selectBestCollections
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
        for k in range(len(conv.kind)):
            for s in range(4):
                for d in range(decks):
                    singleCard = Card(conv, (k, s))
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


