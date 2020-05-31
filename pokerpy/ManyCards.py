import pandas as pd
from pokerpy.SingleCard import Card
from random import shuffle


class SetOfCards:
    """This is a group of cards
        PlayerCards, Deck and Flop are SetOfCards"""
    def __init__(self):
        # create the empty list of cards
        self.cards = []

    def giveSingleCard(self, index=0):
        if index in range(0, len(self.cards)):
            singleCard = self.cards[index]
            self.cards.remove(self.cards[index])
        return singleCard

    def giveCards(self, number):
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

    def takeCards(self, cardsList):
        for singleCard in cardsList:
            self.cards.append(singleCard)

    def showOnConsole(self):
        if not self.cards:
            print('There is no card in this group')
        else:
            for card in self.cards:
                print(card.name)

    def sort(self):
        self.cards.sort()
    # numberOfCards: int
    # faceDownCards: int(?)
    # faceUpCards: int(?)
    # selectedCards
    # show()


class PlayerCards(SetOfCards):
    """look at the class name, it's not so hard"""
    # typePoint()
    # selectBestCollections
    # change()
    # show()


# class Deck(SetOfCards, pd.DataFrame):
# I remove DataFrame due to problems with import abc
class Deck(SetOfCards):
    """Deck is Deck"""
    # This is the constructor
    def __init__(self, lowestcard=2, decks=1):
        # decks=0 => empty deck
        # decks=2 => classic Scala40 deck
        super().__init__()
        lowestRank = lowestcard - 2
        # fulfill the cards list
        for n in range(lowestRank, 13):
            for s in range(4):
                for d in range(0, decks):
                    rankTuple = (n, s)
                    singleCard = Card(rankTuple)
                    self.cards.append(singleCard)
        # create the rejects list (empty at start)
        rejects = []

    def shuffle(self):
        shuffle(self.cards)


class OrderRules:
    # random
    # insert
    # primaGliScarti
    # Sort()
    pass


