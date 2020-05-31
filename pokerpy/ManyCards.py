import pandas as pd
from pokerpy.SingleCard import Card


class SetOfCards:
    """This is a group of cards
        PlayerCards, Deck and Flop are SetOfCards"""
    def __init__(self):
        # create the empty list of cards
        self.cards = []

    def giveSingleCard(self, index=0):
        if index in range(0, len(self.cards)):
            rank = self.cards[index].numberRank, self.cards[index].suitRank
            # I don't know why the next line doesn't work
            # rank = self.cards[index].rank
            self.cards.remove(self.cards[index])
        return rank

    def giveCards(self, number):
        givenCards = []
        # number cannot be lower than zero, nor higher than cards
        number = max(0, number)
        number = min(number, len(self.cards))
        for i in range(number):
            # If there's a new way, I'll be the first in line
            givenCards.append((self.cards[0].numberRank, self.cards[0].suitRank))
            # givenCards.append(self.cards[0].rank)
            self.cards.remove(self.cards[0])
            # self.giveSingleCard(0)
            # givenCards.append(self.giveSingleCard(0))
        return givenCards

    def takeCards(self, cardsList):
        for cardTuple in cardsList:
            number, suit = cardTuple
            self.cards.append(Card(number, suit))

    def showOnConsole(self):
        if not self.cards:
            print('There is no card in this group')
        else:
            for card in self.cards:
                print(card.name)
    # numberOfCards: int
    # faceDownCards: int(?)
    # faceUpCards: int(?)
    # selectedCards: collection(?)
    # giveSelected()
    # change()
    # get()
    # selectCard()
    # show()


class PlayerCards(SetOfCards):
    """look at the class name, it's not so hard"""
    # numberPoint
    # selectBestCollections
    # sort()
    # change()
    # show()
    # typePoint()


# class Deck(SetOfCards, pd.DataFrame):
# I remove DataFrame due to problems with import abc
class Deck(SetOfCards):
    """Deck is Deck"""
    # This is the constructor
    def __init__(self, lowestcard=2, decks=1):
        # decks=0 => empty deck
        # decks=2 => classic Scala40 deck
        super().__init__()
        lowestcard = lowestcard - 2
        # fulfill the cards list
        for n in range(lowestcard, 13):
            for s in range(4):
                for d in range(0, decks):
                    self.cards.append(Card(n, s))
        # create the rejects list (empty at start)
        rejects = []
    # shuffle()
    # create(numberOfPlayers, gameRules)


class OrderRules:
    # random
    # insert
    # primaGliScarti
    # Sort()
    pass


