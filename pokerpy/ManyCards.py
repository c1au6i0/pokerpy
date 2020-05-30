import pandas as pd
from pokerpy.SingleCard import Card


class SetOfCards:
    """This is a group of cards
        PlayerCards, Deck and Flop are SetOfCards"""
    def __init__(self):
        # create the empty list of cards
        self.cards = []

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
        # decks=2 => classic Scala40 deck
        super().__init__()
        lowestcard = lowestcard - 2
        # fulfill the cards list
        for d in range(0, decks):
            for n in range(lowestcard, 13):
                for s in range(4):
                    self.cards.append(Card(n, s))
        # create the rejects list (empty at start)
        rejects = []
    # giveCards()
    # shuffle()
    # create(numberOfPlayers, gameRules)


class OrderRules:
    # random
    # insert
    # primaGliScarti
    # Sort()
    pass


